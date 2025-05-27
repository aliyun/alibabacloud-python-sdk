# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateLabReservationRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        end_time: str = None,
        lab_id: int = None,
        member_count: int = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.lab_id = lab_id
        # This parameter is required.
        self.member_count = member_count
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateLabReservationResponseBodyLabReservation(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateLabReservationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_reservation: CreateLabReservationResponseBodyLabReservation = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.lab_reservation = lab_reservation
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lab_reservation:
            self.lab_reservation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lab_reservation is not None:
            result['LabReservation'] = self.lab_reservation.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LabReservation') is not None:
            temp_model = CreateLabReservationResponseBodyLabReservation()
            self.lab_reservation = temp_model.from_map(m['LabReservation'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLabReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabReservationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLabReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLabSessionRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        lab_id: int = None,
        ram_account_id: int = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.lab_id = lab_id
        # This parameter is required.
        self.ram_account_id = ram_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        if self.ram_account_id is not None:
            result['RamAccountId'] = self.ram_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        if m.get('RamAccountId') is not None:
            self.ram_account_id = m.get('RamAccountId')
        return self


class CreateLabSessionResponseBodyLabSession(TeaModel):
    def __init__(
        self,
        id: str = None,
        url: str = None,
    ):
        self.id = id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateLabSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_session: CreateLabSessionResponseBodyLabSession = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.lab_session = lab_session
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lab_session:
            self.lab_session.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lab_session is not None:
            result['LabSession'] = self.lab_session.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LabSession') is not None:
            temp_model = CreateLabSessionResponseBodyLabSession()
            self.lab_session = temp_model.from_map(m['LabSession'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLabSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLabSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCourseRequest(TeaModel):
    def __init__(
        self,
        course_id: int = None,
    ):
        # This parameter is required.
        self.course_id = course_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.course_id is not None:
            result['CourseId'] = self.course_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CourseId') is not None:
            self.course_id = m.get('CourseId')
        return self


class DescribeCourseResponseBodyCourseChaptersLessons(TeaModel):
    def __init__(
        self,
        duration: int = None,
        id: int = None,
        title: str = None,
        type: str = None,
    ):
        self.duration = duration
        self.id = id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCourseResponseBodyCourseChaptersUnitLessons(TeaModel):
    def __init__(
        self,
        duration: int = None,
        id: int = None,
        title: str = None,
        type: str = None,
    ):
        self.duration = duration
        self.id = id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCourseResponseBodyCourseChaptersUnit(TeaModel):
    def __init__(
        self,
        lessons: List[DescribeCourseResponseBodyCourseChaptersUnitLessons] = None,
        number: int = None,
        title: str = None,
    ):
        self.lessons = lessons
        self.number = number
        self.title = title

    def validate(self):
        if self.lessons:
            for k in self.lessons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lessons'] = []
        if self.lessons is not None:
            for k in self.lessons:
                result['Lessons'].append(k.to_map() if k else None)
        if self.number is not None:
            result['Number'] = self.number
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lessons = []
        if m.get('Lessons') is not None:
            for k in m.get('Lessons'):
                temp_model = DescribeCourseResponseBodyCourseChaptersUnitLessons()
                self.lessons.append(temp_model.from_map(k))
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeCourseResponseBodyCourseChapters(TeaModel):
    def __init__(
        self,
        lessons: List[DescribeCourseResponseBodyCourseChaptersLessons] = None,
        number: int = None,
        title: str = None,
        unit: List[DescribeCourseResponseBodyCourseChaptersUnit] = None,
    ):
        self.lessons = lessons
        self.number = number
        self.title = title
        self.unit = unit

    def validate(self):
        if self.lessons:
            for k in self.lessons:
                if k:
                    k.validate()
        if self.unit:
            for k in self.unit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Lessons'] = []
        if self.lessons is not None:
            for k in self.lessons:
                result['Lessons'].append(k.to_map() if k else None)
        if self.number is not None:
            result['Number'] = self.number
        if self.title is not None:
            result['Title'] = self.title
        result['Unit'] = []
        if self.unit is not None:
            for k in self.unit:
                result['Unit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lessons = []
        if m.get('Lessons') is not None:
            for k in m.get('Lessons'):
                temp_model = DescribeCourseResponseBodyCourseChaptersLessons()
                self.lessons.append(temp_model.from_map(k))
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        self.unit = []
        if m.get('Unit') is not None:
            for k in m.get('Unit'):
                temp_model = DescribeCourseResponseBodyCourseChaptersUnit()
                self.unit.append(temp_model.from_map(k))
        return self


class DescribeCourseResponseBodyCourseLessons(TeaModel):
    def __init__(
        self,
        duration: int = None,
        id: int = None,
        title: str = None,
        type: str = None,
    ):
        self.duration = duration
        self.id = id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCourseResponseBodyCourse(TeaModel):
    def __init__(
        self,
        category: str = None,
        chapters: List[DescribeCourseResponseBodyCourseChapters] = None,
        id: str = None,
        introduction: str = None,
        lesson_num: int = None,
        lessons: List[DescribeCourseResponseBodyCourseLessons] = None,
        picture_url: str = None,
        tags: str = None,
        title: str = None,
    ):
        self.category = category
        self.chapters = chapters
        self.id = id
        self.introduction = introduction
        self.lesson_num = lesson_num
        self.lessons = lessons
        self.picture_url = picture_url
        self.tags = tags
        self.title = title

    def validate(self):
        if self.chapters:
            for k in self.chapters:
                if k:
                    k.validate()
        if self.lessons:
            for k in self.lessons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['Chapters'] = []
        if self.chapters is not None:
            for k in self.chapters:
                result['Chapters'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.lesson_num is not None:
            result['LessonNum'] = self.lesson_num
        result['Lessons'] = []
        if self.lessons is not None:
            for k in self.lessons:
                result['Lessons'].append(k.to_map() if k else None)
        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.chapters = []
        if m.get('Chapters') is not None:
            for k in m.get('Chapters'):
                temp_model = DescribeCourseResponseBodyCourseChapters()
                self.chapters.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LessonNum') is not None:
            self.lesson_num = m.get('LessonNum')
        self.lessons = []
        if m.get('Lessons') is not None:
            for k in m.get('Lessons'):
                temp_model = DescribeCourseResponseBodyCourseLessons()
                self.lessons.append(temp_model.from_map(k))
        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeCourseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        course: DescribeCourseResponseBodyCourse = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.course = course
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.course:
            self.course.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.course is not None:
            result['Course'] = self.course.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Course') is not None:
            temp_model = DescribeCourseResponseBodyCourse()
            self.course = temp_model.from_map(m['Course'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCourseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCourseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCourseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCourseLessonRequest(TeaModel):
    def __init__(
        self,
        lesson_id: int = None,
    ):
        # This parameter is required.
        self.lesson_id = lesson_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lesson_id is not None:
            result['LessonId'] = self.lesson_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LessonId') is not None:
            self.lesson_id = m.get('LessonId')
        return self


class DescribeCourseLessonResponseBodyCourseLesson(TeaModel):
    def __init__(
        self,
        content: str = None,
        url: str = None,
    ):
        self.content = content
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeCourseLessonResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        course_lesson: DescribeCourseLessonResponseBodyCourseLesson = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.course_lesson = course_lesson
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.course_lesson:
            self.course_lesson.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.course_lesson is not None:
            result['CourseLesson'] = self.course_lesson.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CourseLesson') is not None:
            temp_model = DescribeCourseLessonResponseBodyCourseLesson()
            self.course_lesson = temp_model.from_map(m['CourseLesson'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCourseLessonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCourseLessonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCourseLessonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLabRequest(TeaModel):
    def __init__(
        self,
        lab_id: int = None,
    ):
        # This parameter is required.
        self.lab_id = lab_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        return self


class DescribeLabResponseBodyLab(TeaModel):
    def __init__(
        self,
        duration: int = None,
        id: int = None,
        introduction: str = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.duration = duration
        self.id = id
        self.introduction = introduction
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeLabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab: DescribeLabResponseBodyLab = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.lab = lab
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lab:
            self.lab.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lab is not None:
            result['Lab'] = self.lab.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Lab') is not None:
            temp_model = DescribeLabResponseBodyLab()
            self.lab = temp_model.from_map(m['Lab'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLabReservationRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        lab_reservation_id: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.lab_reservation_id = lab_reservation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.lab_reservation_id is not None:
            result['LabReservationId'] = self.lab_reservation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('LabReservationId') is not None:
            self.lab_reservation_id = m.get('LabReservationId')
        return self


class DescribeLabReservationResponseBodyLabReservation(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        end_time: str = None,
        id: str = None,
        member_count: int = None,
        start_time: str = None,
    ):
        self.account_id = account_id
        self.end_time = end_time
        self.id = id
        self.member_count = member_count
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeLabReservationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_reservation: DescribeLabReservationResponseBodyLabReservation = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.lab_reservation = lab_reservation
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lab_reservation:
            self.lab_reservation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lab_reservation is not None:
            result['LabReservation'] = self.lab_reservation.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LabReservation') is not None:
            temp_model = DescribeLabReservationResponseBodyLabReservation()
            self.lab_reservation = temp_model.from_map(m['LabReservation'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLabReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLabReservationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLabReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLabSessionRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        lab_session_id: str = None,
        ram_account_id: int = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.lab_session_id = lab_session_id
        # This parameter is required.
        self.ram_account_id = ram_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.lab_session_id is not None:
            result['LabSessionId'] = self.lab_session_id
        if self.ram_account_id is not None:
            result['RamAccountId'] = self.ram_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('LabSessionId') is not None:
            self.lab_session_id = m.get('LabSessionId')
        if m.get('RamAccountId') is not None:
            self.ram_account_id = m.get('RamAccountId')
        return self


class DescribeLabSessionResponseBodyLabSession(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        finished: bool = None,
        id: str = None,
        lab_id: int = None,
        url: str = None,
    ):
        self.create_time = create_time
        self.finished = finished
        self.id = id
        self.lab_id = lab_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.id is not None:
            result['Id'] = self.id
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeLabSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_session: DescribeLabSessionResponseBodyLabSession = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.lab_session = lab_session
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lab_session:
            self.lab_session.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.lab_session is not None:
            result['LabSession'] = self.lab_session.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LabSession') is not None:
            temp_model = DescribeLabSessionResponseBodyLabSession()
            self.lab_session = temp_model.from_map(m['LabSession'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLabSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLabSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLabSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCoursesRequest(TeaModel):
    def __init__(
        self,
        id: List[int] = None,
        page: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCoursesResponseBodyCourses(TeaModel):
    def __init__(
        self,
        category: str = None,
        id: str = None,
        introduction: str = None,
        lesson_num: int = None,
        picture_url: str = None,
        tags: str = None,
        title: str = None,
    ):
        self.category = category
        self.id = id
        self.introduction = introduction
        self.lesson_num = lesson_num
        self.picture_url = picture_url
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.lesson_num is not None:
            result['LessonNum'] = self.lesson_num
        if self.picture_url is not None:
            result['PictureUrl'] = self.picture_url
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('LessonNum') is not None:
            self.lesson_num = m.get('LessonNum')
        if m.get('PictureUrl') is not None:
            self.picture_url = m.get('PictureUrl')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListCoursesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        courses: List[ListCoursesResponseBodyCourses] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.courses = courses
        self.message = message
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.courses:
            for k in self.courses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Courses'] = []
        if self.courses is not None:
            for k in self.courses:
                result['Courses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.courses = []
        if m.get('Courses') is not None:
            for k in m.get('Courses'):
                temp_model = ListCoursesResponseBodyCourses()
                self.courses.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCoursesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCoursesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCoursesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListLabReservationsRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        page: int = None,
        page_size: int = None,
    ):
        self.account_id = account_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PageListLabReservationsResponseBodyLabReservations(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        end_time: str = None,
        id: str = None,
        member_count: int = None,
        start_time: str = None,
    ):
        self.account_id = account_id
        self.end_time = end_time
        self.id = id
        self.member_count = member_count
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class PageListLabReservationsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_reservations: List[PageListLabReservationsResponseBodyLabReservations] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.lab_reservations = lab_reservations
        self.message = message
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.lab_reservations:
            for k in self.lab_reservations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['LabReservations'] = []
        if self.lab_reservations is not None:
            for k in self.lab_reservations:
                result['LabReservations'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.lab_reservations = []
        if m.get('LabReservations') is not None:
            for k in m.get('LabReservations'):
                temp_model = PageListLabReservationsResponseBodyLabReservations()
                self.lab_reservations.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageListLabReservationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageListLabReservationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PageListLabReservationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListLabSessionsRequest(TeaModel):
    def __init__(
        self,
        finished: bool = None,
        lab_id: int = None,
        page: int = None,
        page_size: int = None,
        ram_account_id: int = None,
    ):
        self.finished = finished
        self.lab_id = lab_id
        self.page = page
        self.page_size = page_size
        self.ram_account_id = ram_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ram_account_id is not None:
            result['RamAccountId'] = self.ram_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RamAccountId') is not None:
            self.ram_account_id = m.get('RamAccountId')
        return self


class PageListLabSessionsResponseBodyLabSessions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        finished: bool = None,
        id: str = None,
        lab_id: int = None,
        url: str = None,
    ):
        self.create_time = create_time
        self.finished = finished
        self.id = id
        self.lab_id = lab_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.id is not None:
            result['Id'] = self.id
        if self.lab_id is not None:
            result['LabId'] = self.lab_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LabId') is not None:
            self.lab_id = m.get('LabId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PageListLabSessionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        lab_sessions: List[PageListLabSessionsResponseBodyLabSessions] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.lab_sessions = lab_sessions
        self.message = message
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.lab_sessions:
            for k in self.lab_sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['LabSessions'] = []
        if self.lab_sessions is not None:
            for k in self.lab_sessions:
                result['LabSessions'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.lab_sessions = []
        if m.get('LabSessions') is not None:
            for k in m.get('LabSessions'):
                temp_model = PageListLabSessionsResponseBodyLabSessions()
                self.lab_sessions.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageListLabSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageListLabSessionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PageListLabSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListLabsRequest(TeaModel):
    def __init__(
        self,
        id: List[int] = None,
        page: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PageListLabsResponseBodyLabs(TeaModel):
    def __init__(
        self,
        duration: int = None,
        id: int = None,
        introduction: str = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.duration = duration
        self.id = id
        self.introduction = introduction
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PageListLabsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        labs: List[PageListLabsResponseBodyLabs] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.labs = labs
        self.message = message
        self.page = page
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.labs:
            for k in self.labs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Labs'] = []
        if self.labs is not None:
            for k in self.labs:
                result['Labs'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.labs = []
        if m.get('Labs') is not None:
            for k in m.get('Labs'):
                temp_model = PageListLabsResponseBodyLabs()
                self.labs.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageListLabsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PageListLabsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PageListLabsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveLabReservationRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        lab_reservation_id: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.lab_reservation_id = lab_reservation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.lab_reservation_id is not None:
            result['LabReservationId'] = self.lab_reservation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('LabReservationId') is not None:
            self.lab_reservation_id = m.get('LabReservationId')
        return self


class RemoveLabReservationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveLabReservationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveLabReservationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveLabReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


