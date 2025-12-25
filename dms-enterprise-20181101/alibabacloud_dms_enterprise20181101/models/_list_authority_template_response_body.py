# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAuthorityTemplateResponseBody(DaraModel):
    def __init__(
        self,
        authority_template_view_list: main_models.ListAuthorityTemplateResponseBodyAuthorityTemplateViewList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tid: int = None,
        total_count: int = None,
    ):
        # The permission templates.
        self.authority_template_view_list = authority_template_view_list
        # The error code that is returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The ID of the tenant.
        self.tid = tid
        # The total number of permission templates.
        self.total_count = total_count

    def validate(self):
        if self.authority_template_view_list:
            self.authority_template_view_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authority_template_view_list is not None:
            result['AuthorityTemplateViewList'] = self.authority_template_view_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityTemplateViewList') is not None:
            temp_model = main_models.ListAuthorityTemplateResponseBodyAuthorityTemplateViewList()
            self.authority_template_view_list = temp_model.from_map(m.get('AuthorityTemplateViewList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorityTemplateResponseBodyAuthorityTemplateViewList(DaraModel):
    def __init__(
        self,
        authority_template_view: List[main_models.ListAuthorityTemplateResponseBodyAuthorityTemplateViewListAuthorityTemplateView] = None,
    ):
        self.authority_template_view = authority_template_view

    def validate(self):
        if self.authority_template_view:
            for v1 in self.authority_template_view:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorityTemplateView'] = []
        if self.authority_template_view is not None:
            for k1 in self.authority_template_view:
                result['AuthorityTemplateView'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authority_template_view = []
        if m.get('AuthorityTemplateView') is not None:
            for k1 in m.get('AuthorityTemplateView'):
                temp_model = main_models.ListAuthorityTemplateResponseBodyAuthorityTemplateViewListAuthorityTemplateView()
                self.authority_template_view.append(temp_model.from_map(k1))

        return self

class ListAuthorityTemplateResponseBodyAuthorityTemplateViewListAuthorityTemplateView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator_id: int = None,
        description: str = None,
        name: str = None,
        template_id: int = None,
    ):
        # The time when the permission template was created. The time is in the yyyy-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # The ID of the user who created the permission template.
        self.creator_id = creator_id
        # The description of the permission template.
        self.description = description
        # The name of the permission template.
        self.name = name
        # The ID of the permission template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

