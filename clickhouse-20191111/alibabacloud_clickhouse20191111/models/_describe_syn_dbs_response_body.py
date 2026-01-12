# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeSynDbsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        syn_dbs: List[main_models.DescribeSynDbsResponseBodySynDbs] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about data synchronization between the ApsaraDB for ClickHouse cluster and an ApsaraDB RDS for MySQL instance.
        self.syn_dbs = syn_dbs
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.syn_dbs:
            for v1 in self.syn_dbs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SynDbs'] = []
        if self.syn_dbs is not None:
            for k1 in self.syn_dbs:
                result['SynDbs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.syn_dbs = []
        if m.get('SynDbs') is not None:
            for k1 in m.get('SynDbs'):
                temp_model = main_models.DescribeSynDbsResponseBodySynDbs()
                self.syn_dbs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSynDbsResponseBodySynDbs(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        rds_id: str = None,
        rds_user_name: str = None,
        rds_vpc_url: str = None,
        syn_db: str = None,
        syn_status: bool = None,
    ):
        # *   When the value **true** is returned for the **SynStatus** parameter, the system does not return the ErrorMsg parameter.
        # *   When the value **false** is returned for the **SynStatus** parameter, the system returns for the ErrorMsg parameter the cause why the data synchronization failed.
        self.error_msg = error_msg
        # The ID of the ApsaraDB RDS for MySQL instance.
        self.rds_id = rds_id
        # The database account that is used to log on to the ApsaraDB RDS for MySQL instance.
        self.rds_user_name = rds_user_name
        # The internal endpoint of the ApsaraDB RDS for MySQL instance.
        self.rds_vpc_url = rds_vpc_url
        # The name of the database in the ApsaraDB RDS for MySQL instance.
        self.syn_db = syn_db
        # Indicates whether the data synchronization succeeded. Valid values:
        # 
        # *   **true**: The data synchronization succeeded.
        # *   **false**: The data synchronization failed.
        self.syn_status = syn_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.rds_id is not None:
            result['RdsId'] = self.rds_id

        if self.rds_user_name is not None:
            result['RdsUserName'] = self.rds_user_name

        if self.rds_vpc_url is not None:
            result['RdsVpcUrl'] = self.rds_vpc_url

        if self.syn_db is not None:
            result['SynDb'] = self.syn_db

        if self.syn_status is not None:
            result['SynStatus'] = self.syn_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RdsId') is not None:
            self.rds_id = m.get('RdsId')

        if m.get('RdsUserName') is not None:
            self.rds_user_name = m.get('RdsUserName')

        if m.get('RdsVpcUrl') is not None:
            self.rds_vpc_url = m.get('RdsVpcUrl')

        if m.get('SynDb') is not None:
            self.syn_db = m.get('SynDb')

        if m.get('SynStatus') is not None:
            self.syn_status = m.get('SynStatus')

        return self

