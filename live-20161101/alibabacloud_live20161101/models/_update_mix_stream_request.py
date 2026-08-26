# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMixStreamRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        input_stream_list: str = None,
        layout_id: str = None,
        mix_stream_id: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The streaming domain.
        # 
        # >Notice: 
        # 
        # Only domain names in the China (Shanghai) and China (Beijing) regions are supported.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The list of input streams for the mix. This is a JSON array.
        # 
        # For more information, see **InputStreamConfig** below.
        # 
        # This parameter is required.
        self.input_stream_list = input_stream_list
        # The layout ID. The following values are supported:
        # 
        # - **MixStreamLayout-1-1**
        # 
        # - **MixStreamLayout-2-1**
        # 
        # - **MixStreamLayout-2-2**
        # 
        # - **MixStreamLayout-2-3**
        # 
        # - **MixStreamLayout-3-1**
        # 
        # - **MixStreamLayout-3-2**
        # 
        # - **MixStreamLayout-4-1**
        # 
        # - **USERDEFINED** (If you use a custom layout instead of a preset layout, set this parameter to this value.)
        self.layout_id = layout_id
        # The ID of the stream mix task. If you created the task by calling the [CreateMixStream](https://help.aliyun.com/document_detail/2848087.html) operation, use the MixStreamId value returned in the response.
        # 
        # This parameter is required.
        self.mix_stream_id = mix_stream_id
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.input_stream_list is not None:
            result['InputStreamList'] = self.input_stream_list

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.mix_stream_id is not None:
            result['MixStreamId'] = self.mix_stream_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InputStreamList') is not None:
            self.input_stream_list = m.get('InputStreamList')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('MixStreamId') is not None:
            self.mix_stream_id = m.get('MixStreamId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

