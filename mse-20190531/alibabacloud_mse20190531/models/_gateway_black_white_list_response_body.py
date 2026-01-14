# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GatewayBlackWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GatewayBlackWhiteListResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 is returned if the request is successful.
        self.code = code
        # The data returned.
        self.data = data
        # The placeholder in the dynamic error message. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        # The error code.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
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

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
            temp_model = main_models.GatewayBlackWhiteListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GatewayBlackWhiteListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.GatewayBlackWhiteListResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The returned information.
        self.result = result
        # The total number of instances returned.
        self.total_size = total_size

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GatewayBlackWhiteListResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class GatewayBlackWhiteListResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_white: bool = None,
        name: str = None,
        note: str = None,
        resource_id: int = None,
        resource_id_json_list: str = None,
        resource_id_name_json: str = None,
        resource_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The content of the blacklist.
        self.content = content
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The time when the blacklist or whitelist was created.
        self.gmt_create = gmt_create
        # The time when the rule was modified.
        self.gmt_modified = gmt_modified
        # The ID of the blacklist and whitelist.
        self.id = id
        # Specifies whether to enable the whitelist feature.
        self.is_white = is_white
        # The name of the blacklist.
        self.name = name
        # The comment.
        self.note = note
        # The resource ID.
        self.resource_id = resource_id
        # The list of resource IDs in the JSON format.
        # 
        # *   If the value of the ResourceType parameter is ROUTE, the value of this parameter is the list of route IDs.
        # *   If the value of the ResourceType parameter is DOMAIN, the value of this parameter is the list of domain names.
        self.resource_id_json_list = resource_id_json_list
        # The description of the resource name.
        self.resource_id_name_json = resource_id_name_json
        # The effective scope of the blacklist or whitelist. Valid values:
        # 
        # *   GATEWAY
        # *   DOMAIN
        # *   ROUTE
        self.resource_type = resource_type
        # The status of the blacklist or whitelist.
        # 
        # *   on
        # *   off
        self.status = status
        # The type of the blacklist and whitelist. The value is fixed to IP address blacklist and whitelist.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.name is not None:
            result['Name'] = self.name

        if self.note is not None:
            result['Note'] = self.note

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_id_json_list is not None:
            result['ResourceIdJsonList'] = self.resource_id_json_list

        if self.resource_id_name_json is not None:
            result['ResourceIdNameJson'] = self.resource_id_name_json

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceIdJsonList') is not None:
            self.resource_id_json_list = m.get('ResourceIdJsonList')

        if m.get('ResourceIdNameJson') is not None:
            self.resource_id_name_json = m.get('ResourceIdNameJson')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

