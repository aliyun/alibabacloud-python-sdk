# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCastersRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        caster_name: str = None,
        charge_type: int = None,
        end_time: str = None,
        norm_type: str = None,
        order_by_modify_asc: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        status: int = None,
        tag: List[main_models.DescribeCastersRequestTag] = None,
    ):
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848012.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the ApsaraVideo Live console and click Production Studios in the left-side navigation pane.
        # 
        # > 
        # 
        # *   You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # *   If you leave this parameter empty, the data of all production studios is returned.
        self.caster_id = caster_id
        # The name of the production studio.
        self.caster_name = caster_name
        # The billing method. Valid values:
        # 
        # *   0: the subscription billing method
        # *   1: the pay-as-you-go billing method
        self.charge_type = charge_type
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The type of the production studio. Valid values:
        # 
        # *   1: general mode
        # *   3: lightweight carousel playback mode
        # *   4: virtual studio
        # *   6: playlist mode
        self.norm_type = norm_type
        # Specifies whether to sort the production studios in ascending order based on the modification time.
        # 
        # >  If you leave this parameter empty, the default value is used. Default value: false.
        self.order_by_modify_asc = order_by_modify_asc
        self.owner_id = owner_id
        # The number of the page to return.
        self.page_num = page_num
        # The number of templates to return on each page. If you leave this parameter empty, the default value is used. Default value: 100.
        self.page_size = page_size
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The status of the production studio. Valid values:
        # 
        # *   0: idle
        # *   1: streaming
        self.status = status
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.caster_name is not None:
            result['CasterName'] = self.caster_name

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.norm_type is not None:
            result['NormType'] = self.norm_type

        if self.order_by_modify_asc is not None:
            result['OrderByModifyAsc'] = self.order_by_modify_asc

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('CasterName') is not None:
            self.caster_name = m.get('CasterName')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NormType') is not None:
            self.norm_type = m.get('NormType')

        if m.get('OrderByModifyAsc') is not None:
            self.order_by_modify_asc = m.get('OrderByModifyAsc')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeCastersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCastersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

