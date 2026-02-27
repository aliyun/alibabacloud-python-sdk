# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListTargetAttachmentsForControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        target_attachments: main_models.ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.target_attachments = target_attachments
        # The total number of objects to which the control policy is attached.
        self.total_count = total_count

    def validate(self):
        if self.target_attachments:
            self.target_attachments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.target_attachments is not None:
            result['TargetAttachments'] = self.target_attachments.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TargetAttachments') is not None:
            temp_model = main_models.ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments()
            self.target_attachments = temp_model.from_map(m.get('TargetAttachments'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachments(DaraModel):
    def __init__(
        self,
        target_attachment: List[main_models.ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment] = None,
    ):
        self.target_attachment = target_attachment

    def validate(self):
        if self.target_attachment:
            for v1 in self.target_attachment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TargetAttachment'] = []
        if self.target_attachment is not None:
            for k1 in self.target_attachment:
                result['TargetAttachment'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_attachment = []
        if m.get('TargetAttachment') is not None:
            for k1 in m.get('TargetAttachment'):
                temp_model = main_models.ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment()
                self.target_attachment.append(temp_model.from_map(k1))

        return self

class ListTargetAttachmentsForControlPolicyResponseBodyTargetAttachmentsTargetAttachment(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
    ):
        self.attach_date = attach_date
        self.target_id = target_id
        self.target_name = target_name
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

