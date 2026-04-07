# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCalcEnginesRequest(DaraModel):
    def __init__(
        self,
        calc_engine_type: str = None,
        env_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
    ):
        # The type of the compute engine. The value of this parameter is not case-sensitive. Valid values:
        # 
        # *   **ODPS**
        # *   **EMR**
        # *   **BLINK**
        # *   **HOLO**
        # *   **MaxGraph**
        # *   **HYBRIDDB_FOR_POSTGRESQL**
        # *   **ADB_MYSQL**
        # *   **HADOOP_CDH**
        # *   **CLICKHOUSE**
        # 
        # This parameter is required.
        self.calc_engine_type = calc_engine_type
        # The environment in which the compute engine is used. Valid values:
        # 
        # *   **DEV**
        # *   **PRD**
        self.env_type = env_type
        # The name of the compute engine, which must be exactly matched.
        self.name = name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace with which the compute engine is associated.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calc_engine_type is not None:
            result['CalcEngineType'] = self.calc_engine_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalcEngineType') is not None:
            self.calc_engine_type = m.get('CalcEngineType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

