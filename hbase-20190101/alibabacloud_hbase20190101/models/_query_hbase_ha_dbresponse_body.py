# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class QueryHBaseHaDBResponseBody(DaraModel):
    def __init__(
        self,
        cluster_list: main_models.QueryHBaseHaDBResponseBodyClusterList = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cluster_list = cluster_list
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = main_models.QueryHBaseHaDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m.get('ClusterList'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryHBaseHaDBResponseBodyClusterList(DaraModel):
    def __init__(
        self,
        cluster: List[main_models.QueryHBaseHaDBResponseBodyClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for v1 in self.cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cluster'] = []
        if self.cluster is not None:
            for k1 in self.cluster:
                result['Cluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k1 in m.get('Cluster'):
                temp_model = main_models.QueryHBaseHaDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k1))

        return self

class QueryHBaseHaDBResponseBodyClusterListCluster(DaraModel):
    def __init__(
        self,
        active_name: str = None,
        bds_name: str = None,
        ha_name: str = None,
        ha_slb_conn_list: main_models.QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList = None,
        standby_name: str = None,
    ):
        self.active_name = active_name
        self.bds_name = bds_name
        self.ha_name = ha_name
        self.ha_slb_conn_list = ha_slb_conn_list
        self.standby_name = standby_name

    def validate(self):
        if self.ha_slb_conn_list:
            self.ha_slb_conn_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_name is not None:
            result['ActiveName'] = self.active_name

        if self.bds_name is not None:
            result['BdsName'] = self.bds_name

        if self.ha_name is not None:
            result['HaName'] = self.ha_name

        if self.ha_slb_conn_list is not None:
            result['HaSlbConnList'] = self.ha_slb_conn_list.to_map()

        if self.standby_name is not None:
            result['StandbyName'] = self.standby_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveName') is not None:
            self.active_name = m.get('ActiveName')

        if m.get('BdsName') is not None:
            self.bds_name = m.get('BdsName')

        if m.get('HaName') is not None:
            self.ha_name = m.get('HaName')

        if m.get('HaSlbConnList') is not None:
            temp_model = main_models.QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList()
            self.ha_slb_conn_list = temp_model.from_map(m.get('HaSlbConnList'))

        if m.get('StandbyName') is not None:
            self.standby_name = m.get('StandbyName')

        return self

class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList(DaraModel):
    def __init__(
        self,
        ha_slb_conn: List[main_models.QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn] = None,
    ):
        self.ha_slb_conn = ha_slb_conn

    def validate(self):
        if self.ha_slb_conn:
            for v1 in self.ha_slb_conn:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HaSlbConn'] = []
        if self.ha_slb_conn is not None:
            for k1 in self.ha_slb_conn:
                result['HaSlbConn'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ha_slb_conn = []
        if m.get('HaSlbConn') is not None:
            for k1 in m.get('HaSlbConn'):
                temp_model = main_models.QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn()
                self.ha_slb_conn.append(temp_model.from_map(k1))

        return self

class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn(DaraModel):
    def __init__(
        self,
        hbase_type: str = None,
        slb_conn_addr: str = None,
        slb_type: str = None,
    ):
        self.hbase_type = hbase_type
        self.slb_conn_addr = slb_conn_addr
        self.slb_type = slb_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type

        if self.slb_conn_addr is not None:
            result['SlbConnAddr'] = self.slb_conn_addr

        if self.slb_type is not None:
            result['SlbType'] = self.slb_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')

        if m.get('SlbConnAddr') is not None:
            self.slb_conn_addr = m.get('SlbConnAddr')

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        return self

