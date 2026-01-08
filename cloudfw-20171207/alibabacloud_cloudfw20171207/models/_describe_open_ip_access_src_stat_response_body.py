# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenIpAccessSrcStatResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[main_models.DescribeOpenIpAccessSrcStatResponseBodyStatList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list
        self.total_count = total_count

    def validate(self):
        if self.stat_list:
            for v1 in self.stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatList'] = []
        if self.stat_list is not None:
            for k1 in self.stat_list:
                result['StatList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stat_list = []
        if m.get('StatList') is not None:
            for k1 in m.get('StatList'):
                temp_model = main_models.DescribeOpenIpAccessSrcStatResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOpenIpAccessSrcStatResponseBodyStatList(DaraModel):
    def __init__(
        self,
        abnormal_src_ip: int = None,
        app: str = None,
        normal_src_ip: int = None,
        port: str = None,
    ):
        self.abnormal_src_ip = abnormal_src_ip
        self.app = app
        self.normal_src_ip = normal_src_ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_src_ip is not None:
            result['AbnormalSrcIp'] = self.abnormal_src_ip

        if self.app is not None:
            result['App'] = self.app

        if self.normal_src_ip is not None:
            result['NormalSrcIp'] = self.normal_src_ip

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalSrcIp') is not None:
            self.abnormal_src_ip = m.get('AbnormalSrcIp')

        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('NormalSrcIp') is not None:
            self.normal_src_ip = m.get('NormalSrcIp')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

