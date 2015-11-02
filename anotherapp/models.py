from django.db import models


class TestModel(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class TestModel2(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BigModel(models.Model):
    SOME_VALUE = '1'
    SOME_CHOICE = (
        (SOME_VALUE, SOME_VALUE),
    )

    testmodel = models.ForeignKey(TestModel, verbose_name="TestModel", null=False, related_name="testmodels")
    testmodel2 = models.ForeignKey(TestModel2, verbose_name="TestModel2", null=True, related_name="more_test_models")
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    some_boolean1 = models.BooleanField(default=True, null=False)
    some_boolean2 = models.BooleanField(default=True, null=False)
    some_boolean3 = models.BooleanField(default=True, null=False)
    some_boolean4 = models.BooleanField(default=True, null=False)
    some_boolean5 = models.BooleanField(default=True, null=False)
    some_boolean6 = models.BooleanField(default=True, null=False)
    some_boolean7 = models.BooleanField(default=True, null=False)
    some_boolean8 = models.BooleanField(default=True, null=False)
    some_boolean9 = models.BooleanField(default=True, null=False)
    some_boolean10 = models.BooleanField(default=True, null=False)

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class FooModel(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class FooModel2(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BigModel2(models.Model):
    SOME_VALUE = '1'
    SOME_CHOICE = (
        (SOME_VALUE, SOME_VALUE),
    )

    foomodel = models.ForeignKey(FooModel, verbose_name="FooModel", null=False, related_name="testmodels")
    foomodel2 = models.ForeignKey(FooModel2, verbose_name="FooModel2", null=True, related_name="more_test_models")
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    some_boolean1 = models.BooleanField(default=True, null=False)
    some_boolean2 = models.BooleanField(default=True, null=False)
    some_boolean3 = models.BooleanField(default=True, null=False)
    some_boolean4 = models.BooleanField(default=True, null=False)
    some_boolean5 = models.BooleanField(default=True, null=False)
    some_boolean6 = models.BooleanField(default=True, null=False)
    some_boolean7 = models.BooleanField(default=True, null=False)
    some_boolean8 = models.BooleanField(default=True, null=False)
    some_boolean9 = models.BooleanField(default=True, null=False)
    some_boolean10 = models.BooleanField(default=True, null=False)

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class BarModel(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BarModel2(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BigModel3(models.Model):
    SOME_VALUE = '1'
    SOME_CHOICE = (
        (SOME_VALUE, SOME_VALUE),
    )

    barmodel = models.ForeignKey(BarModel, verbose_name="BarModel", null=False, related_name="testmodels")
    barmodel2 = models.ForeignKey(BarModel2, verbose_name="BarModel2", null=True, related_name="more_test_models")
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    some_boolean1 = models.BooleanField(default=True, null=False)
    some_boolean2 = models.BooleanField(default=True, null=False)
    some_boolean3 = models.BooleanField(default=True, null=False)
    some_boolean4 = models.BooleanField(default=True, null=False)
    some_boolean5 = models.BooleanField(default=True, null=False)
    some_boolean6 = models.BooleanField(default=True, null=False)
    some_boolean7 = models.BooleanField(default=True, null=False)
    some_boolean8 = models.BooleanField(default=True, null=False)
    some_boolean9 = models.BooleanField(default=True, null=False)
    some_boolean10 = models.BooleanField(default=True, null=False)

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)


class BazModel(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BazModel2(models.Model):
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    is_something = models.BooleanField(default=True, null=False)
    language_code = models.CharField(max_length=10, null=False, blank=False, default='en')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


class BigModel4(models.Model):
    SOME_VALUE = '1'
    SOME_CHOICE = (
        (SOME_VALUE, SOME_VALUE),
    )

    bazmodel = models.ForeignKey(BazModel, verbose_name="BazModel", null=False, related_name="testmodels")
    bazmodel2 = models.ForeignKey(BazModel2, verbose_name="BazModel2", null=True, related_name="more_test_models")
    uuid = models.CharField(max_length=100, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    some_boolean1 = models.BooleanField(default=True, null=False)
    some_boolean2 = models.BooleanField(default=True, null=False)
    some_boolean3 = models.BooleanField(default=True, null=False)
    some_boolean4 = models.BooleanField(default=True, null=False)
    some_boolean5 = models.BooleanField(default=True, null=False)
    some_boolean6 = models.BooleanField(default=True, null=False)
    some_boolean7 = models.BooleanField(default=True, null=False)
    some_boolean8 = models.BooleanField(default=True, null=False)
    some_boolean9 = models.BooleanField(default=True, null=False)
    some_boolean10 = models.BooleanField(default=True, null=False)

    some_msg1 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg2 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg3 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg4 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg5 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg6 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg7 = models.CharField(max_length=1024, null=True, blank=True)
    some_msg8 = models.CharField(max_length=1024, null=True, blank=True)
