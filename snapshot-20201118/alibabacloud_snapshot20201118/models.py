# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, BinaryIO, List


class GetSnapshotBlockRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        block_index: str = None,
        block_token: str = None,
        snapshot_id: str = None,
    ):
        # 幂等参数
        self.client_token = client_token
        # 待读取的数据块索引，从零开始。从 ListChangedBlocks 或者 ListSnapshotBlocks 返回
        self.block_index = block_index
        # 待读取的数据块Token，从零开始。从 ListChangedBlocks 或者 ListSnapshotBlocks 返回
        self.block_token = block_token
        # 待读取数据的快照名称
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.block_token is not None:
            result['BlockToken'] = self.block_token
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('BlockToken') is not None:
            self.block_token = m.get('BlockToken')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class GetSnapshotBlockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BinaryIO = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


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
        self.next_token = next_token
        self.max_results = max_results
        self.client_token = client_token
        self.first_snapshot_id = first_snapshot_id
        self.second_snapshot_id = second_snapshot_id
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
        first_block_token: str = None,
        block_index: int = None,
        second_block_token: str = None,
    ):
        self.first_block_token = first_block_token
        self.block_index = block_index
        self.second_block_token = second_block_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.first_block_token is not None:
            result['FirstBlockToken'] = self.first_block_token
        if self.block_index is not None:
            result['BlockIndex'] = self.block_index
        if self.second_block_token is not None:
            result['SecondBlockToken'] = self.second_block_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstBlockToken') is not None:
            self.first_block_token = m.get('FirstBlockToken')
        if m.get('BlockIndex') is not None:
            self.block_index = m.get('BlockIndex')
        if m.get('SecondBlockToken') is not None:
            self.second_block_token = m.get('SecondBlockToken')
        return self


class ListChangedBlocksResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        expiry_time: int = None,
        block_size: int = None,
        volume_size: int = None,
        changed_blocks: List[ListChangedBlocksResponseBodyChangedBlocks] = None,
    ):
        self.next_token = next_token
        self.expiry_time = expiry_time
        self.block_size = block_size
        self.volume_size = volume_size
        self.changed_blocks = changed_blocks

    def validate(self):
        if self.changed_blocks:
            for k in self.changed_blocks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        result['ChangedBlocks'] = []
        if self.changed_blocks is not None:
            for k in self.changed_blocks:
                result['ChangedBlocks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        self.changed_blocks = []
        if m.get('ChangedBlocks') is not None:
            for k in m.get('ChangedBlocks'):
                temp_model = ListChangedBlocksResponseBodyChangedBlocks()
                self.changed_blocks.append(temp_model.from_map(k))
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


class ListSnapshotBlocksRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        client_token: str = None,
        snapshot_id: str = None,
        starting_block_index: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.client_token = client_token
        self.snapshot_id = snapshot_id
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
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
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
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('StartingBlockIndex') is not None:
            self.starting_block_index = m.get('StartingBlockIndex')
        return self


class ListSnapshotBlocksResponseBodyBlocks(TeaModel):
    def __init__(
        self,
        block_index: int = None,
        block_token: str = None,
    ):
        self.block_index = block_index
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


class ListSnapshotBlocksResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        expiry_time: int = None,
        block_size: int = None,
        volume_size: int = None,
        blocks: List[ListSnapshotBlocksResponseBodyBlocks] = None,
    ):
        self.next_token = next_token
        self.expiry_time = expiry_time
        self.block_size = block_size
        self.volume_size = volume_size
        self.blocks = blocks

    def validate(self):
        if self.blocks:
            for k in self.blocks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.block_size is not None:
            result['BlockSize'] = self.block_size
        if self.volume_size is not None:
            result['VolumeSize'] = self.volume_size
        result['Blocks'] = []
        if self.blocks is not None:
            for k in self.blocks:
                result['Blocks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('BlockSize') is not None:
            self.block_size = m.get('BlockSize')
        if m.get('VolumeSize') is not None:
            self.volume_size = m.get('VolumeSize')
        self.blocks = []
        if m.get('Blocks') is not None:
            for k in m.get('Blocks'):
                temp_model = ListSnapshotBlocksResponseBodyBlocks()
                self.blocks.append(temp_model.from_map(k))
        return self


class ListSnapshotBlocksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSnapshotBlocksResponseBody = None,
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
            temp_model = ListSnapshotBlocksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


