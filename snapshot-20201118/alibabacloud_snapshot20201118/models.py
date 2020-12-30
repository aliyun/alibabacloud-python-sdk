# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListChangedBlocksRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        client_token: str = None,
        first_snapshot_id: str = None,
        second_snapshot_id: str = None,
        starting_block_index: int = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 幂等参数
        self.client_token = client_token
        # 待比较的第一个快照名称
        self.first_snapshot_id = first_snapshot_id
        # 待比较的第二个快照名称
        self.second_snapshot_id = second_snapshot_id
        # 两个快照比较的起始数据块 index，从零开始
        self.starting_block_index = starting_block_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.first_snapshot_id is not None:
            result['FirstSnapshotId'] = self.first_snapshot_id
        if self.second_snapshot_id is not None:
            result['SecondSnapshotId'] = self.second_snapshot_id
        if self.starting_block_index is not None:
            result['StartingBlockIndex'] = self.starting_block_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FirstSnapshotId') is not None:
            self.first_snapshot_id = m.get('FirstSnapshotId')
        if m.get('SecondSnapshotId') is not None:
            self.second_snapshot_id = m.get('SecondSnapshotId')
        if m.get('StartingBlockIndex') is not None:
            self.starting_block_index = m.get('StartingBlockIndex')
        return self


class ListChangedBlocksResponseBodyChangedBlocks(TeaModel):
    def __init__(
        self,
        block_index: int = None,
        block_token: bytes = None,
    ):
        # 数据块的索引值，从零开始
        self.block_index = block_index
        # 数据块的 Token，用于后续的数据读取
        self.block_token = block_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.block_token is not None:
            result['BlockToken'] = self.block_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('BlockToken') is not None:
            self.block_token = m.get('BlockToken')
        return self


class ListChangedBlocksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: bytes = None,
        max_results: int = None,
        changed_blocks: List[ListChangedBlocksResponseBodyChangedBlocks] = None,
        expiry_time: int = None,
        volume_size: int = None,
        block_size: int = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 下一页结果的 token，为空时代表无新增页
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 两个快照差异的数据块列表
        self.changed_blocks = changed_blocks
        # 差异数据块 token 过期时间戳
        self.expiry_time = expiry_time
        # 快照大小，单位 GB，最小 1GB
        self.volume_size = volume_size
        # 数据块大小，单位 Byte
        self.block_size = block_size

    def validate(self):
        if self.changed_blocks:
            for k in self.changed_blocks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ChangedBlocks'] = []
        if self.changed_blocks is not None:
            for k in self.changed_blocks:
                result['ChangedBlocks'].append(k.to_map() if k else None)
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.changed_blocks = []
        if m.get('ChangedBlocks') is not None:
            for k in m.get('ChangedBlocks'):
                temp_model = ListChangedBlocksResponseBodyChangedBlocks()
                self.changed_blocks.append(temp_model.from_map(k))
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        return self


class ListChangedBlocksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChangedBlocksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChangedBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


