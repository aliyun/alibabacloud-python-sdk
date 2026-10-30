# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudPhoneNodePriceRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        count: str = None,
        is_single_img_disk: bool = None,
        period: str = None,
        period_unit: str = None,
        phone_count: int = None,
        phone_data_volume: int = None,
        promotion_id: str = None,
        server_share_data_volume: int = None,
        server_type: str = None,
        swap_size: int = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        self.charge_type = charge_type
        # The number of cloud phone matrices to purchase.
        self.count = count
        # Specifies whether to use a single image disk. Default value: false. Valid values:
        # 
        # - true: Uses only the system disk.
        # 
        # - false: Uses the system disk and the shared internal storage image disk.
        self.is_single_img_disk = is_single_img_disk
        # The subscription period of the resource. The unit is specified by PeriodUnit. Valid values: 1 month, 2 months, 3 months, 6 months, and 1 year.
        self.period = period
        # The unit of the subscription period. Valid values:
        # - **Month**: Month.
        # - **Year**: Year.
        self.period_unit = period_unit
        # The number of provisioned instances, which refers to the number of cloud phone instances in the matrix.
        self.phone_count = phone_count
        # The size of the dedicated internal storage. Unit: GiB.
        self.phone_data_volume = phone_data_volume
        # The promotion ID.
        self.promotion_id = promotion_id
        # The size of the shared internal storage. Unit: GiB.
        # 
        # > The minimum size of the shared internal storage must be greater than the number of instances in the matrix multiplied by 10 GiB.
        self.server_share_data_volume = server_share_data_volume
        # The specifications of the cloud phone matrix.
        # 
        # This parameter is required.
        self.server_type = server_type
        # The size of the swap space.
        self.swap_size = swap_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.count is not None:
            result['Count'] = self.count

        if self.is_single_img_disk is not None:
            result['IsSingleImgDisk'] = self.is_single_img_disk

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.server_share_data_volume is not None:
            result['ServerShareDataVolume'] = self.server_share_data_volume

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.swap_size is not None:
            result['SwapSize'] = self.swap_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('IsSingleImgDisk') is not None:
            self.is_single_img_disk = m.get('IsSingleImgDisk')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ServerShareDataVolume') is not None:
            self.server_share_data_volume = m.get('ServerShareDataVolume')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('SwapSize') is not None:
            self.swap_size = m.get('SwapSize')

        return self

