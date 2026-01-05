# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateCloudPhoneNodeShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth_package_id: str = None,
        bandwidth_package_type: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        count: str = None,
        display_config_shrink: str = None,
        down_bandwidth_limit: int = None,
        image_id: str = None,
        instance_type: str = None,
        is_single_img_disk: bool = None,
        network_id: str = None,
        network_info_shrink: str = None,
        network_type: str = None,
        node_name: str = None,
        period: int = None,
        period_unit: str = None,
        phone_count: int = None,
        phone_data_volume: int = None,
        promotion_id: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        server_share_data_volume: int = None,
        server_type: str = None,
        stream_mode: int = None,
        swap_size: int = None,
        tag: List[main_models.CreateCloudPhoneNodeShrinkRequestTag] = None,
        up_bandwidth_limit: int = None,
        use_template: str = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   False (default): You must manually complete the payment in the Alibaba Cloud Expenses and Costs console.
        # *   true: enables the auto-payment feature.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature.
        # 
        # Valid values:
        # 
        # *   true: enables the auto-renewal feature. In this case, the system automatically renews instances upon expiration.
        # *   false (default): disables the auto-renewal feature. In this case, you need to manually renew instances upon expiration.
        self.auto_renew = auto_renew
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        # The region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method. Only the subscription billing method is supported.
        self.charge_type = charge_type
        # The number of cloud phone matrixes you want to purchase.
        self.count = count
        self.display_config_shrink = display_config_shrink
        self.down_bandwidth_limit = down_bandwidth_limit
        # The image ID.
        self.image_id = image_id
        # The instance specification.
        # 
        # Valid values:
        # 
        # *   ac.max: By default, this specification allows up to 25 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        # *   ac.plus: By default, this specification allows up to 40 instances. You can adjust this number by using PhoneCount (Value range: 4 to 40).
        self.instance_type = instance_type
        self.is_single_img_disk = is_single_img_disk
        # The office network ID.
        self.network_id = network_id
        self.network_info_shrink = network_info_shrink
        self.network_type = network_type
        # The name of the cloud phone matrix.
        self.node_name = node_name
        # The subscription duration. The unit is specified by `PeriodUnit`. Valid values:
        # 
        # *   When `PeriodUnit` is set to **year**: 1.
        # *   When `PeriodUnit` is set to **month**: 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The number of instances per cloud phone matrix.
        self.phone_count = phone_count
        self.phone_data_volume = phone_data_volume
        self.promotion_id = promotion_id
        # The resolution height. Unit: pixel.
        self.resolution_height = resolution_height
        # The resolution width. Unit: pixel.
        self.resolution_width = resolution_width
        # The shared storage size Unit: GiB.
        self.server_share_data_volume = server_share_data_volume
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        # 
        # This parameter is required.
        self.server_type = server_type
        self.stream_mode = stream_mode
        self.swap_size = swap_size
        # The resource tags.
        self.tag = tag
        self.up_bandwidth_limit = up_bandwidth_limit
        self.use_template = use_template
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.count is not None:
            result['Count'] = self.count

        if self.display_config_shrink is not None:
            result['DisplayConfig'] = self.display_config_shrink

        if self.down_bandwidth_limit is not None:
            result['DownBandwidthLimit'] = self.down_bandwidth_limit

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_single_img_disk is not None:
            result['IsSingleImgDisk'] = self.is_single_img_disk

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_info_shrink is not None:
            result['NetworkInfo'] = self.network_info_shrink

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_name is not None:
            result['NodeName'] = self.node_name

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

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.server_share_data_volume is not None:
            result['ServerShareDataVolume'] = self.server_share_data_volume

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.stream_mode is not None:
            result['StreamMode'] = self.stream_mode

        if self.swap_size is not None:
            result['SwapSize'] = self.swap_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.up_bandwidth_limit is not None:
            result['UpBandwidthLimit'] = self.up_bandwidth_limit

        if self.use_template is not None:
            result['UseTemplate'] = self.use_template

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DisplayConfig') is not None:
            self.display_config_shrink = m.get('DisplayConfig')

        if m.get('DownBandwidthLimit') is not None:
            self.down_bandwidth_limit = m.get('DownBandwidthLimit')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsSingleImgDisk') is not None:
            self.is_single_img_disk = m.get('IsSingleImgDisk')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkInfo') is not None:
            self.network_info_shrink = m.get('NetworkInfo')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

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

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('ServerShareDataVolume') is not None:
            self.server_share_data_volume = m.get('ServerShareDataVolume')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('StreamMode') is not None:
            self.stream_mode = m.get('StreamMode')

        if m.get('SwapSize') is not None:
            self.swap_size = m.get('SwapSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCloudPhoneNodeShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UpBandwidthLimit') is not None:
            self.up_bandwidth_limit = m.get('UpBandwidthLimit')

        if m.get('UseTemplate') is not None:
            self.use_template = m.get('UseTemplate')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateCloudPhoneNodeShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

