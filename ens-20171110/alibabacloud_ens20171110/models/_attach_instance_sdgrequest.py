# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class AttachInstanceSDGRequest(DaraModel):
    def __init__(
        self,
        disk_access_protocol: str = None,
        disk_type: str = None,
        instance_ids: List[str] = None,
        load_opt: main_models.AttachInstanceSDGRequestLoadOpt = None,
        sdgid: str = None,
    ):
        self.disk_access_protocol = disk_access_protocol
        self.disk_type = disk_type
        # The IDs of the instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.load_opt = load_opt
        # The ID of the SDG.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        if self.load_opt:
            self.load_opt.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_access_protocol is not None:
            result['DiskAccessProtocol'] = self.disk_access_protocol

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.load_opt is not None:
            result['LoadOpt'] = self.load_opt.to_map()

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskAccessProtocol') is not None:
            self.disk_access_protocol = m.get('DiskAccessProtocol')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LoadOpt') is not None:
            temp_model = main_models.AttachInstanceSDGRequestLoadOpt()
            self.load_opt = temp_model.from_map(m.get('LoadOpt'))

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

class AttachInstanceSDGRequestLoadOpt(DaraModel):
    def __init__(
        self,
        block_rw_split: bool = None,
        block_rw_split_size: int = None,
        cache: bool = None,
        cache_size: int = None,
    ):
        self.block_rw_split = block_rw_split
        self.block_rw_split_size = block_rw_split_size
        self.cache = cache
        self.cache_size = cache_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_rw_split is not None:
            result['BlockRwSplit'] = self.block_rw_split

        if self.block_rw_split_size is not None:
            result['BlockRwSplitSize'] = self.block_rw_split_size

        if self.cache is not None:
            result['Cache'] = self.cache

        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockRwSplit') is not None:
            self.block_rw_split = m.get('BlockRwSplit')

        if m.get('BlockRwSplitSize') is not None:
            self.block_rw_split_size = m.get('BlockRwSplitSize')

        if m.get('Cache') is not None:
            self.cache = m.get('Cache')

        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        return self

