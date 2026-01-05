# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDatabaseNetworksResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeGlobalDatabaseNetworksResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # Details about the GDNs.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeGlobalDatabaseNetworksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGlobalDatabaseNetworksResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dbclusters: List[main_models.DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters] = None,
        dbtype: str = None,
        dbversion: str = None,
        gdndescription: str = None,
        gdnid: str = None,
        gdnstatus: str = None,
        labels: main_models.DescribeGlobalDatabaseNetworksResponseBodyItemsLabels = None,
    ):
        # The time when the GDN was created. The time is in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time
        # Details about clusters in the GDN.
        self.dbclusters = dbclusters
        # The type of the database engine. Only **MySQL** is supported.
        self.dbtype = dbtype
        # The version of the database engine. Only the **8.0** version is supported.
        self.dbversion = dbversion
        # The description of the GDN. The description must meet the following requirements:
        # 
        # *   It cannot start with `http://` or `https://`.
        # *   It must start with a letter.
        # *   It can contain letters, digits, underscores (_), and hyphens (-).
        # *   It must be 2 to 126 characters in length.
        self.gdndescription = gdndescription
        # The ID of the GDN.
        self.gdnid = gdnid
        # The status of the GDN. Valid values:
        # 
        # *   **Creating**: The GDN is being created.
        # *   **active**: The GDN is running.
        # *   **deleting**: The GDN is being deleted.
        # *   **locked**: The GDN is locked. If the GDN is locked, you cannot perform operations on clusters in the GDN.
        # *   **removing_member**: The secondary cluster is being removed from the GDN.
        self.gdnstatus = gdnstatus
        self.labels = labels

    def validate(self):
        if self.dbclusters:
            for v1 in self.dbclusters:
                 if v1:
                    v1.validate()
        if self.labels:
            self.labels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DBClusters'] = []
        if self.dbclusters is not None:
            for k1 in self.dbclusters:
                result['DBClusters'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.gdnstatus is not None:
            result['GDNStatus'] = self.gdnstatus

        if self.labels is not None:
            result['Labels'] = self.labels.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.dbclusters = []
        if m.get('DBClusters') is not None:
            for k1 in m.get('DBClusters'):
                temp_model = main_models.DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters()
                self.dbclusters.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('GDNStatus') is not None:
            self.gdnstatus = m.get('GDNStatus')

        if m.get('Labels') is not None:
            temp_model = main_models.DescribeGlobalDatabaseNetworksResponseBodyItemsLabels()
            self.labels = temp_model.from_map(m.get('Labels'))

        return self

class DescribeGlobalDatabaseNetworksResponseBodyItemsLabels(DaraModel):
    def __init__(
        self,
        gdnversion: str = None,
    ):
        self.gdnversion = gdnversion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gdnversion is not None:
            result['GDNVersion'] = self.gdnversion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GDNVersion') is not None:
            self.gdnversion = m.get('GDNVersion')

        return self

class DescribeGlobalDatabaseNetworksResponseBodyItemsDBClusters(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
        role: str = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster.
        self.region_id = region_id
        # The role of the cluster. Valid values:
        # 
        # *   **Primary**: the primary cluster
        # *   **standby**: the secondary cluster
        # 
        # > A GDN consists of one primary cluster and up to four secondary clusters. For more information, see [GDN](https://help.aliyun.com/document_detail/160381.html).
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

