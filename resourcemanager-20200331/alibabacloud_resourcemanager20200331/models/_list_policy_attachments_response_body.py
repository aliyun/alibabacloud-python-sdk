# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListPolicyAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_attachments: main_models.ListPolicyAttachmentsResponseBodyPolicyAttachments = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        self.policy_attachments = policy_attachments
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policy_attachments:
            self.policy_attachments.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_attachments is not None:
            result['PolicyAttachments'] = self.policy_attachments.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyAttachments') is not None:
            temp_model = main_models.ListPolicyAttachmentsResponseBodyPolicyAttachments()
            self.policy_attachments = temp_model.from_map(m.get('PolicyAttachments'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPolicyAttachmentsResponseBodyPolicyAttachments(DaraModel):
    def __init__(
        self,
        policy_attachment: List[main_models.ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment] = None,
    ):
        self.policy_attachment = policy_attachment

    def validate(self):
        if self.policy_attachment:
            for v1 in self.policy_attachment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyAttachment'] = []
        if self.policy_attachment is not None:
            for k1 in self.policy_attachment:
                result['PolicyAttachment'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_attachment = []
        if m.get('PolicyAttachment') is not None:
            for k1 in m.get('PolicyAttachment'):
                temp_model = main_models.ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment()
                self.policy_attachment.append(temp_model.from_map(k1))

        return self

class ListPolicyAttachmentsResponseBodyPolicyAttachmentsPolicyAttachment(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        principal_name: str = None,
        principal_type: str = None,
        resource_group_id: str = None,
    ):
        self.attach_date = attach_date
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

