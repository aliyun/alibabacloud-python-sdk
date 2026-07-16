# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProjectAttachmentsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeProjectAttachmentsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeProjectAttachmentsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeProjectAttachmentsResponseBodyResult(DaraModel):
    def __init__(
        self,
        attachment_token: str = None,
        attachment_type: str = None,
        content: str = None,
        file_link: str = None,
        file_link_gmt_expired: int = None,
        file_name: str = None,
        file_size: int = None,
        file_suffix: str = None,
        gmt_create: int = None,
        node_id: int = None,
        node_name: str = None,
        operator: int = None,
        operator_name: str = None,
        operator_role: str = None,
        step_no: int = None,
    ):
        self.attachment_token = attachment_token
        self.attachment_type = attachment_type
        self.content = content
        self.file_link = file_link
        self.file_link_gmt_expired = file_link_gmt_expired
        self.file_name = file_name
        self.file_size = file_size
        self.file_suffix = file_suffix
        self.gmt_create = gmt_create
        self.node_id = node_id
        self.node_name = node_name
        self.operator = operator
        self.operator_name = operator_name
        self.operator_role = operator_role
        self.step_no = step_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_token is not None:
            result['AttachmentToken'] = self.attachment_token

        if self.attachment_type is not None:
            result['AttachmentType'] = self.attachment_type

        if self.content is not None:
            result['Content'] = self.content

        if self.file_link is not None:
            result['FileLink'] = self.file_link

        if self.file_link_gmt_expired is not None:
            result['FileLinkGmtExpired'] = self.file_link_gmt_expired

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role

        if self.step_no is not None:
            result['StepNo'] = self.step_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentToken') is not None:
            self.attachment_token = m.get('AttachmentToken')

        if m.get('AttachmentType') is not None:
            self.attachment_type = m.get('AttachmentType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileLink') is not None:
            self.file_link = m.get('FileLink')

        if m.get('FileLinkGmtExpired') is not None:
            self.file_link_gmt_expired = m.get('FileLinkGmtExpired')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')

        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')

        return self

