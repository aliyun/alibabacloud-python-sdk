# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLServerUpgradeVersionsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeSQLServerUpgradeVersionsResponseBodyItems = None,
        request_id: str = None,
    ):
        self.items = items
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        current_version: str = None,
        sqlserver_upgrade_versions: main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersions = None,
    ):
        # 当前的版本。若传DBInstanceId，则返回实例版本。若未传DBInstanceId，但传了EngineVersion，则返回EngineVersion。
        self.current_version = current_version
        # 一个列表，显示是否支持升级到目标版本
        self.sqlserver_upgrade_versions = sqlserver_upgrade_versions

    def validate(self):
        if self.sqlserver_upgrade_versions:
            self.sqlserver_upgrade_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.sqlserver_upgrade_versions is not None:
            result['SQLServerUpgradeVersions'] = self.sqlserver_upgrade_versions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('SQLServerUpgradeVersions') is not None:
            temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersions()
            self.sqlserver_upgrade_versions = temp_model.from_map(m.get('SQLServerUpgradeVersions'))

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersions(DaraModel):
    def __init__(
        self,
        sqlserver_upgrade_version: List[main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersion] = None,
    ):
        self.sqlserver_upgrade_version = sqlserver_upgrade_version

    def validate(self):
        if self.sqlserver_upgrade_version:
            for v1 in self.sqlserver_upgrade_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLServerUpgradeVersion'] = []
        if self.sqlserver_upgrade_version is not None:
            for k1 in self.sqlserver_upgrade_version:
                result['SQLServerUpgradeVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlserver_upgrade_version = []
        if m.get('SQLServerUpgradeVersion') is not None:
            for k1 in m.get('SQLServerUpgradeVersion'):
                temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersion()
                self.sqlserver_upgrade_version.append(temp_model.from_map(k1))

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersion(DaraModel):
    def __init__(
        self,
        dbinstance_class_items: main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItems = None,
        enable_upgrade: str = None,
        version: str = None,
    ):
        # 一个列表，描述了每个版本是否可以成为升级目标
        self.dbinstance_class_items = dbinstance_class_items
        # 是否支持升级到该版本
        self.enable_upgrade = enable_upgrade
        # 版本值
        self.version = version

    def validate(self):
        if self.dbinstance_class_items:
            self.dbinstance_class_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_class_items is not None:
            result['DBInstanceClassItems'] = self.dbinstance_class_items.to_map()

        if self.enable_upgrade is not None:
            result['EnableUpgrade'] = self.enable_upgrade

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClassItems') is not None:
            temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItems()
            self.dbinstance_class_items = temp_model.from_map(m.get('DBInstanceClassItems'))

        if m.get('EnableUpgrade') is not None:
            self.enable_upgrade = m.get('EnableUpgrade')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItems(DaraModel):
    def __init__(
        self,
        dbinstance_class_item: List[main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItemsDBInstanceClassItem] = None,
    ):
        self.dbinstance_class_item = dbinstance_class_item

    def validate(self):
        if self.dbinstance_class_item:
            for v1 in self.dbinstance_class_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceClassItem'] = []
        if self.dbinstance_class_item is not None:
            for k1 in self.dbinstance_class_item:
                result['DBInstanceClassItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_class_item = []
        if m.get('DBInstanceClassItem') is not None:
            for k1 in m.get('DBInstanceClassItem'):
                temp_model = main_models.DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItemsDBInstanceClassItem()
                self.dbinstance_class_item.append(temp_model.from_map(k1))

        return self

class DescribeSQLServerUpgradeVersionsResponseBodyItemsItemSQLServerUpgradeVersionsSQLServerUpgradeVersionDBInstanceClassItemsDBInstanceClassItem(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        dbinstance_class: str = None,
        dbinstance_class_type: str = None,
        group: str = None,
        memory: str = None,
    ):
        # 可升级的版本规格的CPU大小
        self.cpu = cpu
        # 可升级的版本规格
        self.dbinstance_class = dbinstance_class
        # 可升级的版本规格的类型
        self.dbinstance_class_type = dbinstance_class_type
        # 组类型
        self.group = group
        # 可升级的版本规格的内存大小
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_class_type is not None:
            result['DBInstanceClassType'] = self.dbinstance_class_type

        if self.group is not None:
            result['Group'] = self.group

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceClassType') is not None:
            self.dbinstance_class_type = m.get('DBInstanceClassType')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

