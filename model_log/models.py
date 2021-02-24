from django.db import models


class Log(models.Model):

    ACTIONS = (
        ('C', "Created"),
        ('U', "Updated"),
        ('D', "Deleted")
    )

    date_created = models.DateTimeField("Date created", db_index=True, auto_now_add=True,
                                        help_text="The date and time this changes was.")
    object_id = models.IntegerField(help_text="Primary key of the object under version control.")
    model = models.CharField(help_text="Model of the object under version control.", max_length=128)
    data = models.TextField(blank=True, null=True, help_text="The data being changed.")
    action = models.CharField("Action", choices=ACTIONS, help_text='created|updated|deleted', max_length=1)
    user = models.TextField(blank=True, null=True, help_text='ID of the user who makes the action')

    def __str__(self):
        return "Changes on {} of {} at {}".format(self.object_id, self.object,
                                                  self.date_created.strftime('%Y-%m-%d %H:%M'))

    class Meta:
        ordering = ("-pk",)

