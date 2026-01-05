# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBLinksResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dblink_infos: List[main_models.DescribeDBLinksResponseBodyDBLinkInfos] = None,
        request_id: str = None,
    ):
        # The ID of the cluster.
        self.dbinstance_name = dbinstance_name
        # Details about the database links.
        self.dblink_infos = dblink_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dblink_infos:
            for v1 in self.dblink_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['DBLinkInfos'] = []
        if self.dblink_infos is not None:
            for k1 in self.dblink_infos:
                result['DBLinkInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.dblink_infos = []
        if m.get('DBLinkInfos') is not None:
            for k1 in m.get('DBLinkInfos'):
                temp_model = main_models.DescribeDBLinksResponseBodyDBLinkInfos()
                self.dblink_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBLinksResponseBodyDBLinkInfos(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dblink_name: str = None,
        source_dbname: str = None,
        target_account: str = None,
        target_dbinstance_name: str = None,
        target_dbname: str = None,
    ):
        # The ID of the source cluster that the database link connects.
        self.dbinstance_name = dbinstance_name
        # The name of the database link.
        self.dblink_name = dblink_name
        # The name of the source database of the database link.
        self.source_dbname = source_dbname
        # The account of the destination database of the database link.
        self.target_account = target_account
        # The ID of the destination cluster that the database link connects.
        # 
        # > If the destination cluster is not a PolarDB for Oracle cluster, the returned value is empty.
        self.target_dbinstance_name = target_dbinstance_name
        # The name of the destination database of the database link.
        self.target_dbname = target_dbname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name

        if self.source_dbname is not None:
            result['SourceDBName'] = self.source_dbname

        if self.target_account is not None:
            result['TargetAccount'] = self.target_account

        if self.target_dbinstance_name is not None:
            result['TargetDBInstanceName'] = self.target_dbinstance_name

        if self.target_dbname is not None:
            result['TargetDBName'] = self.target_dbname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')

        if m.get('SourceDBName') is not None:
            self.source_dbname = m.get('SourceDBName')

        if m.get('TargetAccount') is not None:
            self.target_account = m.get('TargetAccount')

        if m.get('TargetDBInstanceName') is not None:
            self.target_dbinstance_name = m.get('TargetDBInstanceName')

        if m.get('TargetDBName') is not None:
            self.target_dbname = m.get('TargetDBName')

        return self

