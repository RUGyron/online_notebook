from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import \
    User, StudentGroup, StudentStream, GroupInStream, Course, Lesson, StudentLessonResult,\
    Section, ClassmatesCheckedTask, TaskOption, StudentResult, Check, TaskWithTick, \
    TaskWithTickOption, TaskWithTickStudentResult, TaskWithClassmatesCheck, TaskWithTeacherCheck, \
    TaskWithKeyword, TaskWithClassmatesCheckOption, TaskWithTeacherCheckOption, TaskWithKeywordOption, \
    TaskWithClassmatesCheckResult, TaskWithTeacherCheckResult, TaskWithKeywordResult


admin.site.register(StudentGroup)
admin.site.register(StudentStream)
admin.site.register(GroupInStream)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(StudentLessonResult)
admin.site.register(Section)
admin.site.register(ClassmatesCheckedTask)
admin.site.register(TaskOption)
admin.site.register(StudentResult)
admin.site.register(Check)
admin.site.register(TaskWithTick)
admin.site.register(TaskWithTickOption)
admin.site.register(TaskWithTickStudentResult)
admin.site.register(TaskWithClassmatesCheck)
admin.site.register(TaskWithTeacherCheck)
admin.site.register(TaskWithKeyword)
admin.site.register(TaskWithClassmatesCheckOption)
admin.site.register(TaskWithTeacherCheckOption)
admin.site.register(TaskWithKeywordOption)
admin.site.register(TaskWithClassmatesCheckResult)
admin.site.register(TaskWithTeacherCheckResult)
admin.site.register(TaskWithKeywordResult)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('role', 'group')}),
admin.site.register(User, UserAdmin)
# admin.site.register(Membership)
