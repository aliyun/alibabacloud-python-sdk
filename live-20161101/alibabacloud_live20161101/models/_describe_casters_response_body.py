# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCastersResponseBody(DaraModel):
    def __init__(
        self,
        caster_list: main_models.DescribeCastersResponseBodyCasterList = None,
        request_id: str = None,
        total: int = None,
    ):
        # The production studios.
        self.caster_list = caster_list
        # The request ID.
        self.request_id = request_id
        # The number of production studios.
        self.total = total

    def validate(self):
        if self.caster_list:
            self.caster_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_list is not None:
            result['CasterList'] = self.caster_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterList') is not None:
            temp_model = main_models.DescribeCastersResponseBodyCasterList()
            self.caster_list = temp_model.from_map(m.get('CasterList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCastersResponseBodyCasterList(DaraModel):
    def __init__(
        self,
        caster: List[main_models.DescribeCastersResponseBodyCasterListCaster] = None,
    ):
        self.caster = caster

    def validate(self):
        if self.caster:
            for v1 in self.caster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Caster'] = []
        if self.caster is not None:
            for k1 in self.caster:
                result['Caster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.caster = []
        if m.get('Caster') is not None:
            for k1 in m.get('Caster'):
                temp_model = main_models.DescribeCastersResponseBodyCasterListCaster()
                self.caster.append(temp_model.from_map(k1))

        return self

class DescribeCastersResponseBodyCasterListCaster(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        caster_name: str = None,
        caster_template: str = None,
        channel_enable: int = None,
        charge_type: str = None,
        client_token_id: str = None,
        create_time: str = None,
        duration: str = None,
        expire_time: str = None,
        last_modified: str = None,
        norm_type: int = None,
        purchase_time: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        status: int = None,
        tags: main_models.DescribeCastersResponseBodyCasterListCasterTags = None,
    ):
        # The ID of the production studio. You can specify the ID in a request to query the streaming URLs of the production studio, start the production studio, add a video resource, a layout, a component, or a playlist to the production studio, or query layouts of the production studio.
        self.caster_id = caster_id
        # The name of the production studio.
        self.caster_name = caster_name
        # The resolution in which the production studio plays videos. This parameter is returned if the subscription billing method is used. Valid values:
        # 
        # *   lp_ld: low definition
        # *   lp_sd: standard definition
        # *   lp_hd: high definition
        # *   lp_ud: ultra high definition.
        # *   lp_ld_v: low definition (portrait mode)
        # *   lp_sd_v: standard definition (portrait mode)
        # *   lp_hd_v: high definition (portrait mode)
        # *   lp_ud_v: ultra high definition (portrait mode)
        self.caster_template = caster_template
        # Indicates whether the channel is enabled for the production studio.
        # 
        # *   0: The channel is disabled.
        # *   1: The channel is enabled.
        self.channel_enable = channel_enable
        # The billing method. Valid values:
        # 
        # *   PrePaid: the subscription billing method
        # *   PostPaid: the pay-as-you-go billing method
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        self.client_token_id = client_token_id
        # The time when the production studio was created.
        self.create_time = create_time
        # The streaming duration. Format: hh:mm:ss.
        self.duration = duration
        # The time when the production studio expires.
        self.expire_time = expire_time
        # The time when the production studio was last modified. For example, the time when the production studio was last started, stopped, or modified is returned.
        self.last_modified = last_modified
        # The type of the production studio. Valid values:
        # 
        # *   0: playlist mode
        # *   1: general mode
        self.norm_type = norm_type
        # The time when the production studio was purchased.
        self.purchase_time = purchase_time
        # The resource group ID. For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        # The time when the production studio was started. This parameter is returned if the production studio is in the streaming status.
        self.start_time = start_time
        # The status of the production studio. Valid values:
        # 
        # *   0: idle
        # *   1: streaming
        self.status = status
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.caster_name is not None:
            result['CasterName'] = self.caster_name

        if self.caster_template is not None:
            result['CasterTemplate'] = self.caster_template

        if self.channel_enable is not None:
            result['ChannelEnable'] = self.channel_enable

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token_id is not None:
            result['ClientTokenId'] = self.client_token_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.norm_type is not None:
            result['NormType'] = self.norm_type

        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('CasterName') is not None:
            self.caster_name = m.get('CasterName')

        if m.get('CasterTemplate') is not None:
            self.caster_template = m.get('CasterTemplate')

        if m.get('ChannelEnable') is not None:
            self.channel_enable = m.get('ChannelEnable')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientTokenId') is not None:
            self.client_token_id = m.get('ClientTokenId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('NormType') is not None:
            self.norm_type = m.get('NormType')

        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCastersResponseBodyCasterListCasterTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeCastersResponseBodyCasterListCasterTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCastersResponseBodyCasterListCasterTagsTag] = None,
    ):
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
        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.DescribeCastersResponseBodyCasterListCasterTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCastersResponseBodyCasterListCasterTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

