# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeStoragePoolInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeStoragePoolInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeStoragePoolInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeStoragePoolInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        storage_pools: List[main_models.DescribeStoragePoolInfoResponseBodyDataStoragePools] = None,
    ):
        self.storage_pools = storage_pools

    def validate(self):
        if self.storage_pools:
            for v1 in self.storage_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StoragePools'] = []
        if self.storage_pools is not None:
            for k1 in self.storage_pools:
                result['StoragePools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_pools = []
        if m.get('StoragePools') is not None:
            for k1 in m.get('StoragePools'):
                temp_model = main_models.DescribeStoragePoolInfoResponseBodyDataStoragePools()
                self.storage_pools.append(temp_model.from_map(k1))

        return self

class DescribeStoragePoolInfoResponseBodyDataStoragePools(DaraModel):
    def __init__(
        self,
        class_: str = None,
        dn_id_list: List[str] = None,
        dn_id_string: str = None,
        extra: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        idle_dnid_list: List[str] = None,
        name: str = None,
        un_deletable_dnid: str = None,
    ):
        self.class_ = class_
        self.dn_id_list = dn_id_list
        # DN id
        self.dn_id_string = dn_id_string
        self.extra = extra
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.idle_dnid_list = idle_dnid_list
        self.name = name
        self.un_deletable_dnid = un_deletable_dnid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['Class'] = self.class_

        if self.dn_id_list is not None:
            result['DnIdList'] = self.dn_id_list

        if self.dn_id_string is not None:
            result['DnIdString'] = self.dn_id_string

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.idle_dnid_list is not None:
            result['IdleDNIdList'] = self.idle_dnid_list

        if self.name is not None:
            result['Name'] = self.name

        if self.un_deletable_dnid is not None:
            result['UnDeletableDNId'] = self.un_deletable_dnid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')

        if m.get('DnIdList') is not None:
            self.dn_id_list = m.get('DnIdList')

        if m.get('DnIdString') is not None:
            self.dn_id_string = m.get('DnIdString')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IdleDNIdList') is not None:
            self.idle_dnid_list = m.get('IdleDNIdList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UnDeletableDNId') is not None:
            self.un_deletable_dnid = m.get('UnDeletableDNId')

        return self

