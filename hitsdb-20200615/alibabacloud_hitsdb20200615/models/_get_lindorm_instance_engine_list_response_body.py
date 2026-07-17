# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetLindormInstanceEngineListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        engine_list: List[main_models.GetLindormInstanceEngineListResponseBodyEngineList] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The list of engine types.
        self.engine_list = engine_list
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.engine_list:
            for v1 in self.engine_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['EngineList'] = []
        if self.engine_list is not None:
            for k1 in self.engine_list:
                result['EngineList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.engine_list = []
        if m.get('EngineList') is not None:
            for k1 in m.get('EngineList'):
                temp_model = main_models.GetLindormInstanceEngineListResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLindormInstanceEngineListResponseBodyEngineList(DaraModel):
    def __init__(
        self,
        engine_type: str = None,
        net_info_list: List[main_models.GetLindormInstanceEngineListResponseBodyEngineListNetInfoList] = None,
    ):
        # The engine type. Valid values:
        # 
        # - **lindorm**: LindormTable.
        # 
        # - **tsdb**: LindormTSDB.
        # 
        # - **solr**: Search engine.
        # 
        # - **store**: File engine.
        self.engine_type = engine_type
        # The list of database connection information for the engine.
        self.net_info_list = net_info_list

    def validate(self):
        if self.net_info_list:
            for v1 in self.net_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        result['NetInfoList'] = []
        if self.net_info_list is not None:
            for k1 in self.net_info_list:
                result['NetInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        self.net_info_list = []
        if m.get('NetInfoList') is not None:
            for k1 in m.get('NetInfoList'):
                temp_model = main_models.GetLindormInstanceEngineListResponseBodyEngineListNetInfoList()
                self.net_info_list.append(temp_model.from_map(k1))

        return self

class GetLindormInstanceEngineListResponseBodyEngineListNetInfoList(DaraModel):
    def __init__(
        self,
        access_type: int = None,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
    ):
        # The connection method for LindormTable. Valid values:
        # 
        # - **0**: This is the default value and can be ignored.
        # 
        # - **1**: Use the HBase Java API to access LindormTable.
        # 
        # - **2**: Use a non-Java HBase API to access LindormTable.
        # 
        # - **3**: Use CQL to access LindormTable.
        # 
        # - **4**: Use the LindormTable SQL endpoint.
        # 
        # - **5**: Use the S3-compatible endpoint for LindormTable.
        # 
        # - **6**: Use the MySQL-compatible endpoint for LindormTable.
        self.access_type = access_type
        # The database endpoint.
        self.connection_string = connection_string
        # The network type of the database endpoint. Valid values:
        # 
        # - **0**: Internet.
        # 
        # - **2**: Virtual private cloud (VPC).
        self.net_type = net_type
        # The port number of the database endpoint.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

