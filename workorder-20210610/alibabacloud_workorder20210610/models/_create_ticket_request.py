# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20210610 import models as main_models
from darabonba.model import DaraModel

class CreateTicketRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        creator_id: str = None,
        description: str = None,
        email: str = None,
        file_name_list: List[str] = None,
        secret_info: main_models.CreateTicketRequestSecretInfo = None,
        severity: int = None,
        title: str = None,
    ):
        # The ID of the problem category. You can obtain the returned value from the ListCategories operation by using the CategoryId parameter.
        # 
        # This parameter is required.
        self.category_id = category_id
        # Submit the Alibaba Cloud UID of the account, which is required for the MPK virtual market scene.
        self.creator_id = creator_id
        # The description of the ticket. Only pure text format is supported.
        # 
        # This parameter is required.
        self.description = description
        # sdahkjdshga@qq.com
        self.email = email
        # The list of attachment names, GetAttachmentUploadUrl the ObjectKey field returned by the interface.
        self.file_name_list = file_name_list
        # Sensitive information
        self.secret_info = secret_info
        # Enumeration value, 1 for general problem, 2 for urgent problem
        # 
        # Enumeration values:
        # 
        # *   1: regular.
        # *   2: emergency.
        # 
        # This parameter is required.
        self.severity = severity
        # The title of the ticket.
        self.title = title

    def validate(self):
        if self.secret_info:
            self.secret_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list

        if self.secret_info is not None:
            result['SecretInfo'] = self.secret_info.to_map()

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')

        if m.get('SecretInfo') is not None:
            temp_model = main_models.CreateTicketRequestSecretInfo()
            self.secret_info = temp_model.from_map(m.get('SecretInfo'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self



class CreateTicketRequestSecretInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name_list: List[str] = None,
    ):
        # Sensitive information-text content
        self.content = content
        # Sensitive Information-Attachment Name List
        self.file_name_list = file_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')

        return self

