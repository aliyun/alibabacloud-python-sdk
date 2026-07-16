# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetOrganizationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetOrganizationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Data') is not None:
            temp_model = main_models.GetOrganizationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOrganizationResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        namespace_id: str = None,
        org_id: str = None,
        owner_biz_account_id: str = None,
        owner_id: str = None,
        status: str = None,
    ):
        # The organization description.
        self.description = description
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The organization name.
        self.name = name
        # The product namespace ID.
        self.namespace_id = namespace_id
        # The organization ID.
        self.org_id = org_id
        # The business account identifier of the organization owner. The value is aliyunUid for the ALIYUN type and userIdentifier for the SSO type.
        self.owner_biz_account_id = owner_biz_account_id
        # The UAC account ID of the organization owner.
        self.owner_id = owner_id
        # The status. Valid values: ACTIVE and FROZEN.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.owner_biz_account_id is not None:
            result['OwnerBizAccountId'] = self.owner_biz_account_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OwnerBizAccountId') is not None:
            self.owner_biz_account_id = m.get('OwnerBizAccountId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

