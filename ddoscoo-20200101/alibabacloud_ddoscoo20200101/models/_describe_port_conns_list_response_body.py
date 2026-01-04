# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortConnsListResponseBody(DaraModel):
    def __init__(
        self,
        conns_list: List[main_models.DescribePortConnsListResponseBodyConnsList] = None,
        request_id: str = None,
    ):
        # Details about the connections established over the port.
        self.conns_list = conns_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.conns_list:
            for v1 in self.conns_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnsList'] = []
        if self.conns_list is not None:
            for k1 in self.conns_list:
                result['ConnsList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conns_list = []
        if m.get('ConnsList') is not None:
            for k1 in m.get('ConnsList'):
                temp_model = main_models.DescribePortConnsListResponseBodyConnsList()
                self.conns_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortConnsListResponseBodyConnsList(DaraModel):
    def __init__(
        self,
        act_conns: int = None,
        conns: int = None,
        cps: int = None,
        in_act_conns: int = None,
        index: int = None,
    ):
        # The number of active connections.
        self.act_conns = act_conns
        # >  This parameter is in internal preview. Do not use this parameter.
        self.conns = conns
        # The number of new connections.
        self.cps = cps
        # The number of inactive connections.
        self.in_act_conns = in_act_conns
        # The index number of the returned data.
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns

        if self.conns is not None:
            result['Conns'] = self.conns

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')

        if m.get('Conns') is not None:
            self.conns = m.get('Conns')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

