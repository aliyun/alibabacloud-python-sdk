# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListApiPluginsResponseBody(DaraModel):
    def __init__(
        self,
        api_plugins: List[main_models.ListApiPluginsResponseBodyApiPlugins] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.api_plugins = api_plugins
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.api_plugins:
            for v1 in self.api_plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiPlugins'] = []
        if self.api_plugins is not None:
            for k1 in self.api_plugins:
                result['ApiPlugins'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

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
        self.api_plugins = []
        if m.get('ApiPlugins') is not None:
            for k1 in m.get('ApiPlugins'):
                temp_model = main_models.ListApiPluginsResponseBodyApiPlugins()
                self.api_plugins.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApiPluginsResponseBodyApiPlugins(DaraModel):
    def __init__(
        self,
        description: str = None,
        drafted_config_json: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        name: str = None,
        published_config_json: str = None,
        status: str = None,
        type: str = None,
        uuid: str = None,
    ):
        self.description = description
        self.drafted_config_json = drafted_config_json
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.name = name
        self.published_config_json = published_config_json
        self.status = status
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.drafted_config_json is not None:
            result['DraftedConfigJson'] = self.drafted_config_json

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.published_config_json is not None:
            result['PublishedConfigJson'] = self.published_config_json

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DraftedConfigJson') is not None:
            self.drafted_config_json = m.get('DraftedConfigJson')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishedConfigJson') is not None:
            self.published_config_json = m.get('PublishedConfigJson')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

