# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudSiemAssetsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeCloudSiemAssetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeCloudSiemAssetsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudSiemAssetsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeCloudSiemAssetsResponseBodyDataPageInfo = None,
        response_data: List[main_models.DescribeCloudSiemAssetsResponseBodyDataResponseData] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The detailed data.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCloudSiemAssetsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.DescribeCloudSiemAssetsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class DescribeCloudSiemAssetsResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_uuid: str = None,
        aliuid: int = None,
        asset_id: str = None,
        asset_info: List[main_models.DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo] = None,
        asset_name: str = None,
        asset_type: str = None,
        cloud_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        sub_user_id: int = None,
    ):
        # The UUID of the alert associated with the event.
        self.alert_uuid = alert_uuid
        # The ID of the Alibaba Cloud account in SIEM.
        self.aliuid = aliuid
        # The logical ID of the asset.
        self.asset_id = asset_id
        # The display information of the asset is in the JSON format.
        self.asset_info = asset_info
        # The name of the asset.
        self.asset_name = asset_name
        # The type of the asset. Valid values:
        # 
        # *   ip
        # *   domain
        # *   url
        # *   process
        # *   file
        # *   host
        self.asset_type = asset_type
        # The cloud code of the entity. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        # The time when the asset was synchronized.
        self.gmt_create = gmt_create
        # The time when the asset was last updated.
        self.gmt_modified = gmt_modified
        # The ID of the asset.
        self.id = id
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The ID of the associated account to which the asset belongs.
        self.sub_user_id = sub_user_id

    def validate(self):
        if self.asset_info:
            for v1 in self.asset_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        result['AssetInfo'] = []
        if self.asset_info is not None:
            for k1 in self.asset_info:
                result['AssetInfo'].append(k1.to_map() if k1 else None)

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        self.asset_info = []
        if m.get('AssetInfo') is not None:
            for k1 in m.get('AssetInfo'):
                temp_model = main_models.DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo()
                self.asset_info.append(temp_model.from_map(k1))

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

class DescribeCloudSiemAssetsResponseBodyDataResponseDataAssetInfo(DaraModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        # The attribute key.
        self.key = key
        # The name of the key.
        self.key_name = key_name
        # The value of the key.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class DescribeCloudSiemAssetsResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

