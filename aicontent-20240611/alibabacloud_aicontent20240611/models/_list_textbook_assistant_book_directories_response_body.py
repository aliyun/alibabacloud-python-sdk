# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ListTextbookAssistantBookDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListTextbookAssistantBookDirectoriesResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        directory_tree: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree] = None,
        edition_info: main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo = None,
    ):
        self.directory_tree = directory_tree
        self.edition_info = edition_info

    def validate(self):
        if self.directory_tree:
            for v1 in self.directory_tree:
                 if v1:
                    v1.validate()
        if self.edition_info:
            self.edition_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['directoryTree'] = []
        if self.directory_tree is not None:
            for k1 in self.directory_tree:
                result['directoryTree'].append(k1.to_map() if k1 else None)

        if self.edition_info is not None:
            result['editionInfo'] = self.edition_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directory_tree = []
        if m.get('directoryTree') is not None:
            for k1 in m.get('directoryTree'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree()
                self.directory_tree.append(temp_model.from_map(k1))

        if m.get('editionInfo') is not None:
            temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo()
            self.edition_info = temp_model.from_map(m.get('editionInfo'))

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataEditionInfo(DaraModel):
    def __init__(
        self,
        book_id: str = None,
        book_volume: str = None,
        edition: str = None,
        grade: str = None,
        impression: str = None,
        isbn: str = None,
        publisher: str = None,
        subject: str = None,
        version: str = None,
    ):
        self.book_id = book_id
        self.book_volume = book_volume
        self.edition = edition
        self.grade = grade
        self.impression = impression
        self.isbn = isbn
        self.publisher = publisher
        self.subject = subject
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_id is not None:
            result['bookId'] = self.book_id

        if self.book_volume is not None:
            result['bookVolume'] = self.book_volume

        if self.edition is not None:
            result['edition'] = self.edition

        if self.grade is not None:
            result['grade'] = self.grade

        if self.impression is not None:
            result['impression'] = self.impression

        if self.isbn is not None:
            result['isbn'] = self.isbn

        if self.publisher is not None:
            result['publisher'] = self.publisher

        if self.subject is not None:
            result['subject'] = self.subject

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')

        if m.get('bookVolume') is not None:
            self.book_volume = m.get('bookVolume')

        if m.get('edition') is not None:
            self.edition = m.get('edition')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('impression') is not None:
            self.impression = m.get('impression')

        if m.get('isbn') is not None:
            self.isbn = m.get('isbn')

        if m.get('publisher') is not None:
            self.publisher = m.get('publisher')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTree(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        directory_name: str = None,
        topic: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic] = None,
        unit: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit] = None,
    ):
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.topic = topic
        self.unit = unit

    def validate(self):
        if self.topic:
            for v1 in self.topic:
                 if v1:
                    v1.validate()
        if self.unit:
            for v1 in self.unit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_name is not None:
            result['directoryName'] = self.directory_name

        result['topic'] = []
        if self.topic is not None:
            for k1 in self.topic:
                result['topic'].append(k1.to_map() if k1 else None)

        result['unit'] = []
        if self.unit is not None:
            for k1 in self.unit:
                result['unit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')

        self.topic = []
        if m.get('topic') is not None:
            for k1 in m.get('topic'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic()
                self.topic.append(temp_model.from_map(k1))

        self.unit = []
        if m.get('unit') is not None:
            for k1 in m.get('unit'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit()
                self.unit.append(temp_model.from_map(k1))

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnit(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        directory_name: str = None,
        section: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection] = None,
        topic: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic] = None,
    ):
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.section = section
        self.topic = topic

    def validate(self):
        if self.section:
            for v1 in self.section:
                 if v1:
                    v1.validate()
        if self.topic:
            for v1 in self.topic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_name is not None:
            result['directoryName'] = self.directory_name

        result['section'] = []
        if self.section is not None:
            for k1 in self.section:
                result['section'].append(k1.to_map() if k1 else None)

        result['topic'] = []
        if self.topic is not None:
            for k1 in self.topic:
                result['topic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')

        self.section = []
        if m.get('section') is not None:
            for k1 in m.get('section'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection()
                self.section.append(temp_model.from_map(k1))

        self.topic = []
        if m.get('topic') is not None:
            for k1 in m.get('topic'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic()
                self.topic.append(temp_model.from_map(k1))

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitTopic(DaraModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_id is not None:
            result['labelId'] = self.label_id

        if self.label_name is not None:
            result['labelName'] = self.label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')

        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSection(DaraModel):
    def __init__(
        self,
        children: Any = None,
        directory_id: str = None,
        directory_name: str = None,
        topic: List[main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic] = None,
    ):
        self.children = children
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.topic = topic

    def validate(self):
        if self.topic:
            for v1 in self.topic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['children'] = self.children

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_name is not None:
            result['directoryName'] = self.directory_name

        result['topic'] = []
        if self.topic is not None:
            for k1 in self.topic:
                result['topic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryName') is not None:
            self.directory_name = m.get('directoryName')

        self.topic = []
        if m.get('topic') is not None:
            for k1 in m.get('topic'):
                temp_model = main_models.ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic()
                self.topic.append(temp_model.from_map(k1))

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeUnitSectionTopic(DaraModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_id is not None:
            result['labelId'] = self.label_id

        if self.label_name is not None:
            result['labelName'] = self.label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')

        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')

        return self

class ListTextbookAssistantBookDirectoriesResponseBodyDataDirectoryTreeTopic(DaraModel):
    def __init__(
        self,
        label_id: str = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_id is not None:
            result['labelId'] = self.label_id

        if self.label_name is not None:
            result['labelName'] = self.label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')

        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')

        return self

