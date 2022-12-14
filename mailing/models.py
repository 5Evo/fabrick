from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Status(models.Model):
    """
    The Class (model for DB) for Tags
    """
    objects = models.Manager()
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    """
    The Class (model for DB) for Tags
    """
    objects = models.Manager()
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'


class MobileCode(models.Model):
    """
    The Class (model for DB) for Mobile Code
    """
    objects = models.Manager()
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f'{self.code}'


class Mailing(models.Model):
    """
    The Class (model for DB) for mailing
    """
    objects = models.Manager()

    start_time = models.DateTimeField()  # время запуска рассылки
    stop_time = models.DateTimeField()  # Время окончания рассылки
    text_message = models.TextField()  # Сообщение
    filter_mobile = models.ForeignKey(MobileCode, null=True,
                                      on_delete=models.CASCADE)  # фильтр по мобильному оператору получателя
    filter_tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)  # фильтр по тэгу
    create = models.DateTimeField(auto_now_add=True)  # время cоздания рассылки (для статисики и поиска)
    update = models.DateTimeField(auto_now=True)  # время изменения рассылки (для статисики и поиска)

    def save(self, *args, **kwargs):
        """
        Переопределим метод save, чтобы при сохранении рассылки мы могли ее запустить или поставить в очередь
        """
        import datetime
        now = datetime.datetime.now()
        if self.start_time.timestamp() < now.timestamp() < self.stop_time.timestamp():
            self.send_message(now)
        else:
            self.put_in_queue(now)
        super(Mailing, self).save(*args, **kwargs)

    def send_message(self, now):
        """
        TODO: Запускаем рассылку
        :param now: текущее время
        :return:
        """
        print(f'{self.id} start: {self.start_time}, now: {now}, stop: {self.stop_time}')
        pass

    def put_in_queue(self, now):
        """
        TODO: Постановка рассылки в очередь
        :param now: текущее время
        :return:
        """
        print(f'{self.id} NOT NOW {now}')
        pass


class Client(models.Model):
    """
    The Class (model for DB) for Clients
    """
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    objects = models.Manager()
    phone = models.PhoneNumberField()
    mobile_code = models.ForeignKey(MobileCode, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)  # у каждого клиента может быть несколько Тэгов
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')


class Message(models.Model):
    """
    The Class (model for DB) for messages
    """

    objects = models.Manager()
    create = models.DateTimeField(auto_now_add=True)  # время cоздания Сообщения
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    id_mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
