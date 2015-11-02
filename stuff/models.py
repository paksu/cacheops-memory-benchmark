from django.db import models
import uuid

# Create your models here.


class SomeModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('uuid', 'content')

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class SomeRelatedModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')


class SomeAnotherRelatedModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')


class SomeAnotherRelatedModel2(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')
        unique_together = ('f1', 'f2')


class SomeModel2(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('content', 'uuid')


class SomeRelatedModel2(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel2)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')
        unique_together = ('f1', 'f2')


class SomeModel3(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('content', 'uuid')

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class SomeRelatedModel3(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel3)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')
        unique_together = ('f1', 'f2')


class SomeModel4(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('content', 'uuid')


class SomeRelatedModel4(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel4)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')
        unique_together = ('f1', 'f2')


class SomeModel5(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('content', 'uuid')

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class SomeRelatedModel5(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    question = models.ForeignKey(SomeModel5)
    content = models.CharField(max_length=200)
    f1 = models.CharField(max_length=200)
    f2 = models.CharField(max_length=200)
    f3 = models.CharField(max_length=200)
    f4 = models.CharField(max_length=200)
    f5 = models.CharField(max_length=200)
    f6 = models.CharField(max_length=200)
    f7 = models.CharField(max_length=200, null=True, blank=True)
    f8 = models.CharField(max_length=200, null=True, blank=True)
    counter = models.IntegerField(default=0)
    counter2 = models.IntegerField(default=0)

    class Meta:
        unique_together = ('f1', 'question')
        unique_together = ('f1', 'f2')
