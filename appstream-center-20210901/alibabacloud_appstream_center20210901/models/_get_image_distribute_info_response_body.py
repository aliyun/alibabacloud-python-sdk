# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetImageDistributeInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetImageDistributeInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code of the API. A value of 200 indicates success. If the call fails, the corresponding error code is returned.
        self.code = code
        # The image information returned by the query.
        self.data = data
        # The processing information returned by the API.
        self.message = message
        # The request ID, which is used to locate and troubleshoot the request.
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values: true: Successful. false: Failed.
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
            temp_model = main_models.GetImageDistributeInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetImageDistributeInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        image_region_distribute_list: List[main_models.GetImageDistributeInfoResponseBodyDataImageRegionDistributeList] = None,
        image_region_list: List[str] = None,
        image_source: str = None,
    ):
        # The list of region distribution information for the image version.
        self.image_region_distribute_list = image_region_distribute_list
        # The list of region IDs supported by the image.
        self.image_region_list = image_region_list
        # The source of the image. For example, center indicates the central image service.
        self.image_source = image_source

    def validate(self):
        if self.image_region_distribute_list:
            for v1 in self.image_region_distribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageRegionDistributeList'] = []
        if self.image_region_distribute_list is not None:
            for k1 in self.image_region_distribute_list:
                result['ImageRegionDistributeList'].append(k1.to_map() if k1 else None)

        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list

        if self.image_source is not None:
            result['ImageSource'] = self.image_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_region_distribute_list = []
        if m.get('ImageRegionDistributeList') is not None:
            for k1 in m.get('ImageRegionDistributeList'):
                temp_model = main_models.GetImageDistributeInfoResponseBodyDataImageRegionDistributeList()
                self.image_region_distribute_list.append(temp_model.from_map(k1))

        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')

        if m.get('ImageSource') is not None:
            self.image_source = m.get('ImageSource')

        return self

class GetImageDistributeInfoResponseBodyDataImageRegionDistributeList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        ecs_image_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        message: str = None,
        progress: str = None,
        region_id: str = None,
        status: str = None,
        unit_image_id: str = None,
        version_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the image belongs. The account ID for a system image is 0.
        self.ali_uid = ali_uid
        # The ID of the ECS image corresponding to the region.
        self.ecs_image_id = ecs_image_id
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The image ID.
        self.image_id = image_id
        # The processing information reported by the region distribution task.
        self.message = message
        # The distribution progress of the image in the region, expressed as a percentage.
        self.progress = progress
        # The ID of the region to which the image is distributed.
        self.region_id = region_id
        # The region distribution status.
        self.status = status
        # The logical ID of the image on the unit side, which can be different from the central image ID.
        self.unit_image_id = unit_image_id
        # The image version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.ecs_image_id is not None:
            result['EcsImageId'] = self.ecs_image_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.unit_image_id is not None:
            result['UnitImageId'] = self.unit_image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EcsImageId') is not None:
            self.ecs_image_id = m.get('EcsImageId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnitImageId') is not None:
            self.unit_image_id = m.get('UnitImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

