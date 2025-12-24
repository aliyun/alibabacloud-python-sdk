# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMixStreamRequest(DaraModel):
    def __init__(
        self,
        callback_config: str = None,
        domain_name: str = None,
        input_stream_list: str = None,
        layout_id: str = None,
        output_config: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The callback URL. The value is a JSON array. If a callback event is triggered, ApsaraVideo Live sends an HTTP POST request to the URL. The content is included in the HTTP request body.
        self.callback_config = callback_config
        # The main streaming domain.
        # 
        # >  Only domain names that reside in the China (Shanghai) and China (Beijing) regions are supported.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The input streams. The value is a JSON array.
        # 
        # For more information, see **InputStreamConfig**.
        # 
        # This parameter is required.
        self.input_stream_list = input_stream_list
        # The ID of the layout. Valid values:
        # 
        # *   **MixStreamLayout-1-1**
        # *   **MixStreamLayout-2-1**
        # *   **MixStreamLayout-2-2**
        # *   **MixStreamLayout-2-3**
        # *   **MixStreamLayout-3-1**
        # *   **MixStreamLayout-3-2**
        # *   **MixStreamLayout-4-1**
        # *   **USERDEFINED**: If you do not use a preset layout, set this parameter to **USERDEFINED**.
        # 
        # >  For more information, see [Preset layouts for stream mixing](https://help.aliyun.com/document_detail/199361.html).
        # 
        # This parameter is required.
        self.layout_id = layout_id
        # The configuration of the output stream. The value is a JSON string.
        # 
        # For more information, see **OutputConfig**.
        # 
        # This parameter is required.
        self.output_config = output_config
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.input_stream_list is not None:
            result['InputStreamList'] = self.input_stream_list

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            self.callback_config = m.get('CallbackConfig')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InputStreamList') is not None:
            self.input_stream_list = m.get('InputStreamList')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

