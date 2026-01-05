# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeImageListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeImageListResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The images.
        self.data = data
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeImageListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageListResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_biz_tags: List[main_models.DescribeImageListResponseBodyDataImageBizTags] = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_map: Dict[str, main_models.DataImageRegionDistributeMapValue] = None,
        image_region_list: List[str] = None,
        image_type: str = None,
        image_version: str = None,
        language: str = None,
        release_time: str = None,
        rendering_type: str = None,
        status: str = None,
        system_type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The description of the image.
        self.description = description
        # The time when the image was created.
        self.gmt_create = gmt_create
        # The time when the image was last modified.
        self.gmt_modified = gmt_modified
        self.image_biz_tags = image_biz_tags
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The region where the image is distributed. The key is the region and the value is the distribution information.
        self.image_region_distribute_map = image_region_distribute_map
        # The list of regions.
        self.image_region_list = image_region_list
        # The type of the image.
        # 
        # Valid values:
        # 
        # *   User: custom images.
        # *   System: system images.
        self.image_type = image_type
        self.image_version = image_version
        # The language of the image.
        self.language = language
        # The time when the image was published.
        self.release_time = release_time
        # The rendering type.
        # 
        # Valid values:
        # 
        # *   GPURemote
        # *   CPU
        # *   GPULocal
        self.rendering_type = rendering_type
        # The state of the image.
        # 
        # Valid values:
        # 
        # *   AVAILABLE: The image is available.
        # *   DELETE: The image is deleted.
        # *   INIT: The image is being initialized.
        # *   CREATE_FAILED: The image failed to be created.
        # *   CREATING: The image is being created.
        self.status = status
        # The OS type of the image.
        self.system_type = system_type

    def validate(self):
        if self.image_biz_tags:
            for v1 in self.image_biz_tags:
                 if v1:
                    v1.validate()
        if self.image_region_distribute_map:
            for v1 in self.image_region_distribute_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        result['ImageBizTags'] = []
        if self.image_biz_tags is not None:
            for k1 in self.image_biz_tags:
                result['ImageBizTags'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        result['ImageRegionDistributeMap'] = {}
        if self.image_region_distribute_map is not None:
            for k1, v1 in self.image_region_distribute_map.items():
                result['ImageRegionDistributeMap'][k1] = v1.to_map() if v1 else None

        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.language is not None:
            result['Language'] = self.language

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.rendering_type is not None:
            result['RenderingType'] = self.rendering_type

        if self.status is not None:
            result['Status'] = self.status

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        self.image_biz_tags = []
        if m.get('ImageBizTags') is not None:
            for k1 in m.get('ImageBizTags'):
                temp_model = main_models.DescribeImageListResponseBodyDataImageBizTags()
                self.image_biz_tags.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.image_region_distribute_map = {}
        if m.get('ImageRegionDistributeMap') is not None:
            for k1, v1 in m.get('ImageRegionDistributeMap').items():
                temp_model = main_models.DataImageRegionDistributeMapValue()
                self.image_region_distribute_map[k1] = temp_model.from_map(v1)

        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RenderingType') is not None:
            self.rendering_type = m.get('RenderingType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

class DescribeImageListResponseBodyDataImageBizTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

