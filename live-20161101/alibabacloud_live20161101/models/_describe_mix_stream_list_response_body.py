# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeMixStreamListResponseBody(DaraModel):
    def __init__(
        self,
        mix_stream_list: List[main_models.DescribeMixStreamListResponseBodyMixStreamList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # Details about the stream mixing tasks.
        self.mix_stream_list = mix_stream_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of tasks.
        self.total = total

    def validate(self):
        if self.mix_stream_list:
            for v1 in self.mix_stream_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MixStreamList'] = []
        if self.mix_stream_list is not None:
            for k1 in self.mix_stream_list:
                result['MixStreamList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mix_stream_list = []
        if m.get('MixStreamList') is not None:
            for k1 in m.get('MixStreamList'):
                temp_model = main_models.DescribeMixStreamListResponseBodyMixStreamList()
                self.mix_stream_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMixStreamListResponseBodyMixStreamList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        input_stream_number: int = None,
        layout_id: str = None,
        mix_stream_template: str = None,
        mixstream_id: str = None,
        stream_name: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The time when the stream mixing task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the stream mixing task was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The number of input streams.
        self.input_stream_number = input_stream_number
        # The ID of the layout.
        self.layout_id = layout_id
        # The stream mixing template.
        self.mix_stream_template = mix_stream_template
        # The ID of the stream mixing task. You can specify this parameter in a request to delete the steam mixing task.
        self.mixstream_id = mixstream_id
        # The name of the output stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.input_stream_number is not None:
            result['InputStreamNumber'] = self.input_stream_number

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.mix_stream_template is not None:
            result['MixStreamTemplate'] = self.mix_stream_template

        if self.mixstream_id is not None:
            result['MixstreamId'] = self.mixstream_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InputStreamNumber') is not None:
            self.input_stream_number = m.get('InputStreamNumber')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('MixStreamTemplate') is not None:
            self.mix_stream_template = m.get('MixStreamTemplate')

        if m.get('MixstreamId') is not None:
            self.mixstream_id = m.get('MixstreamId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

