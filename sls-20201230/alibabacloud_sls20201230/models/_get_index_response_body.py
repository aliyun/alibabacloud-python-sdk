# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetIndexResponseBody(DaraModel):
    def __init__(
        self,
        index_mode: str = None,
        keys: Dict[str, main_models.IndexKey] = None,
        last_modify_time: int = None,
        line: main_models.GetIndexResponseBodyLine = None,
        log_reduce: bool = None,
        log_reduce_black_list: List[str] = None,
        log_reduce_white_list: List[str] = None,
        max_text_len: int = None,
        storage: str = None,
        ttl: int = None,
    ):
        # The type of the index.
        self.index_mode = index_mode
        # The configurations of field indexes. A field index is in the key-value format in which the key specifies the name of the field and the value specifies the index configuration of the field.
        self.keys = keys
        # The time when the index configurations were last updated. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The configurations of full-text indexes.
        self.line = line
        # Indicates whether the log clustering feature is enabled.
        self.log_reduce = log_reduce
        # The fields in the blacklist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_black_list = log_reduce_black_list
        # The fields in the whitelist that are used to cluster logs. This parameter is valid only if the log clustering feature is enabled.
        self.log_reduce_white_list = log_reduce_white_list
        # The maximum length of a field value that can be retained. Default value: 2048. Unit: bytes. The default value is equal to 2 KB. You can change the value of the max_text_len parameter. Valid values: 64 to 16384. Unit: bytes.
        self.max_text_len = max_text_len
        # The storage type. The value is fixed as pg.
        self.storage = storage
        # The lifecycle of the index file. Valid values: 7, 30, and 90. Unit: day.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.keys:
            for v1 in self.keys.values():
                 if v1:
                    v1.validate()
        if self.line:
            self.line.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_mode is not None:
            result['index_mode'] = self.index_mode

        result['keys'] = {}
        if self.keys is not None:
            for k1, v1 in self.keys.items():
                result['keys'][k1] = v1.to_map() if v1 else None

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.line is not None:
            result['line'] = self.line.to_map()

        if self.log_reduce is not None:
            result['log_reduce'] = self.log_reduce

        if self.log_reduce_black_list is not None:
            result['log_reduce_black_list'] = self.log_reduce_black_list

        if self.log_reduce_white_list is not None:
            result['log_reduce_white_list'] = self.log_reduce_white_list

        if self.max_text_len is not None:
            result['max_text_len'] = self.max_text_len

        if self.storage is not None:
            result['storage'] = self.storage

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index_mode') is not None:
            self.index_mode = m.get('index_mode')

        self.keys = {}
        if m.get('keys') is not None:
            for k1, v1 in m.get('keys').items():
                temp_model = main_models.IndexKey()
                self.keys[k1] = temp_model.from_map(v1)

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('line') is not None:
            temp_model = main_models.GetIndexResponseBodyLine()
            self.line = temp_model.from_map(m.get('line'))

        if m.get('log_reduce') is not None:
            self.log_reduce = m.get('log_reduce')

        if m.get('log_reduce_black_list') is not None:
            self.log_reduce_black_list = m.get('log_reduce_black_list')

        if m.get('log_reduce_white_list') is not None:
            self.log_reduce_white_list = m.get('log_reduce_white_list')

        if m.get('max_text_len') is not None:
            self.max_text_len = m.get('max_text_len')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

class GetIndexResponseBodyLine(DaraModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        chn: bool = None,
        exclude_keys: List[str] = None,
        include_keys: List[str] = None,
        token: List[str] = None,
    ):
        # Indicates whether case sensitivity is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.case_sensitive = case_sensitive
        # Indicates whether Chinese characters are included. Valid values:
        # 
        # *   true
        # *   false
        self.chn = chn
        # The excluded fields.
        self.exclude_keys = exclude_keys
        # The included fields.
        self.include_keys = include_keys
        # The delimiters.
        # 
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.chn is not None:
            result['chn'] = self.chn

        if self.exclude_keys is not None:
            result['exclude_keys'] = self.exclude_keys

        if self.include_keys is not None:
            result['include_keys'] = self.include_keys

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('exclude_keys') is not None:
            self.exclude_keys = m.get('exclude_keys')

        if m.get('include_keys') is not None:
            self.include_keys = m.get('include_keys')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

