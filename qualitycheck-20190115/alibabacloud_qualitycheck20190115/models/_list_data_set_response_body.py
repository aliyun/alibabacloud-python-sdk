# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListDataSetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: main_models.ListDataSetResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        messages: main_models.ListDataSetResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.messages is not None:
            result['Messages'] = self.messages.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Data') is not None:
            temp_model = main_models.ListDataSetResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            temp_model = main_models.ListDataSetResponseBodyMessages()
            self.messages = temp_model.from_map(m.get('Messages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataSetResponseBodyMessages(DaraModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ListDataSetResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataSetResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataSetResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class ListDataSetResponseBodyDataData(DaraModel):
    def __init__(
        self,
        auto_transcoding: int = None,
        channel_id_0: int = None,
        channel_id_1: int = None,
        channel_type: int = None,
        create_time: str = None,
        create_type: int = None,
        data_set_type: int = None,
        is_delete: int = None,
        role_config_prop: str = None,
        role_config_status: int = None,
        role_config_task: str = None,
        set_bucket_name: str = None,
        set_domain: str = None,
        set_folder_name: str = None,
        set_id: int = None,
        set_name: str = None,
        set_number: int = None,
        set_role_arn: str = None,
        set_type: int = None,
        source_data_type: int = None,
        sub_dir: str = None,
        update_time: str = None,
        user_group: str = None,
    ):
        self.auto_transcoding = auto_transcoding
        self.channel_id_0 = channel_id_0
        self.channel_id_1 = channel_id_1
        self.channel_type = channel_type
        self.create_time = create_time
        self.create_type = create_type
        self.data_set_type = data_set_type
        self.is_delete = is_delete
        self.role_config_prop = role_config_prop
        self.role_config_status = role_config_status
        self.role_config_task = role_config_task
        self.set_bucket_name = set_bucket_name
        self.set_domain = set_domain
        self.set_folder_name = set_folder_name
        self.set_id = set_id
        self.set_name = set_name
        self.set_number = set_number
        self.set_role_arn = set_role_arn
        self.set_type = set_type
        self.source_data_type = source_data_type
        self.sub_dir = sub_dir
        self.update_time = update_time
        self.user_group = user_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_transcoding is not None:
            result['AutoTranscoding'] = self.auto_transcoding

        if self.channel_id_0 is not None:
            result['ChannelId0'] = self.channel_id_0

        if self.channel_id_1 is not None:
            result['ChannelId1'] = self.channel_id_1

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.role_config_prop is not None:
            result['RoleConfigProp'] = self.role_config_prop

        if self.role_config_status is not None:
            result['RoleConfigStatus'] = self.role_config_status

        if self.role_config_task is not None:
            result['RoleConfigTask'] = self.role_config_task

        if self.set_bucket_name is not None:
            result['SetBucketName'] = self.set_bucket_name

        if self.set_domain is not None:
            result['SetDomain'] = self.set_domain

        if self.set_folder_name is not None:
            result['SetFolderName'] = self.set_folder_name

        if self.set_id is not None:
            result['SetId'] = self.set_id

        if self.set_name is not None:
            result['SetName'] = self.set_name

        if self.set_number is not None:
            result['SetNumber'] = self.set_number

        if self.set_role_arn is not None:
            result['SetRoleArn'] = self.set_role_arn

        if self.set_type is not None:
            result['SetType'] = self.set_type

        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type

        if self.sub_dir is not None:
            result['SubDir'] = self.sub_dir

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoTranscoding') is not None:
            self.auto_transcoding = m.get('AutoTranscoding')

        if m.get('ChannelId0') is not None:
            self.channel_id_0 = m.get('ChannelId0')

        if m.get('ChannelId1') is not None:
            self.channel_id_1 = m.get('ChannelId1')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('RoleConfigProp') is not None:
            self.role_config_prop = m.get('RoleConfigProp')

        if m.get('RoleConfigStatus') is not None:
            self.role_config_status = m.get('RoleConfigStatus')

        if m.get('RoleConfigTask') is not None:
            self.role_config_task = m.get('RoleConfigTask')

        if m.get('SetBucketName') is not None:
            self.set_bucket_name = m.get('SetBucketName')

        if m.get('SetDomain') is not None:
            self.set_domain = m.get('SetDomain')

        if m.get('SetFolderName') is not None:
            self.set_folder_name = m.get('SetFolderName')

        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')

        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')

        if m.get('SetNumber') is not None:
            self.set_number = m.get('SetNumber')

        if m.get('SetRoleArn') is not None:
            self.set_role_arn = m.get('SetRoleArn')

        if m.get('SetType') is not None:
            self.set_type = m.get('SetType')

        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')

        if m.get('SubDir') is not None:
            self.sub_dir = m.get('SubDir')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        return self

