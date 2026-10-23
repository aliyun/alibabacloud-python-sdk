# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListWorkItemArtifactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListWorkItemArtifactsResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The list of historical artifacts.
        self.items = items
        # The error message.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The total number of returned artifacts.
        self.total_count = total_count

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
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListWorkItemArtifactsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListWorkItemArtifactsResponseBodyItems(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_key: str = None,
        attempt_seq: int = None,
        content_type: str = None,
        created_at: str = None,
        node_key: str = None,
        plan_id: str = None,
        ref: main_models.ListWorkItemArtifactsResponseBodyItemsRef = None,
        run_id: str = None,
        sha_256: str = None,
        size_bytes: int = None,
        summary: str = None,
        title: str = None,
        turn_seq: int = None,
        type: str = None,
        work_item_id: str = None,
    ):
        # The artifact ID.
        self.artifact_id = artifact_id
        # The artifact key.
        self.artifact_key = artifact_key
        # The node attempt sequence number.
        self.attempt_seq = attempt_seq
        # The content type.
        self.content_type = content_type
        # The creation time in ISO 8601 format.
        self.created_at = created_at
        # The node key.
        self.node_key = node_key
        # The plan ID.
        self.plan_id = plan_id
        # The reference information.
        self.ref = ref
        # The run ID.
        self.run_id = run_id
        # The SHA-256 hash of the content.
        self.sha_256 = sha_256
        # The artifact size in bytes.
        self.size_bytes = size_bytes
        # The artifact summary.
        self.summary = summary
        # The artifact title.
        self.title = title
        # The session turn sequence number.
        self.turn_seq = turn_seq
        # The artifact type.
        self.type = type
        # The work item ID.
        self.work_item_id = work_item_id

    def validate(self):
        if self.ref:
            self.ref.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.artifact_key is not None:
            result['artifactKey'] = self.artifact_key

        if self.attempt_seq is not None:
            result['attemptSeq'] = self.attempt_seq

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.node_key is not None:
            result['nodeKey'] = self.node_key

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.ref is not None:
            result['ref'] = self.ref.to_map()

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.sha_256 is not None:
            result['sha256'] = self.sha_256

        if self.size_bytes is not None:
            result['sizeBytes'] = self.size_bytes

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.turn_seq is not None:
            result['turnSeq'] = self.turn_seq

        if self.type is not None:
            result['type'] = self.type

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('artifactKey') is not None:
            self.artifact_key = m.get('artifactKey')

        if m.get('attemptSeq') is not None:
            self.attempt_seq = m.get('attemptSeq')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('nodeKey') is not None:
            self.node_key = m.get('nodeKey')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('ref') is not None:
            temp_model = main_models.ListWorkItemArtifactsResponseBodyItemsRef()
            self.ref = temp_model.from_map(m.get('ref'))

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('sha256') is not None:
            self.sha_256 = m.get('sha256')

        if m.get('sizeBytes') is not None:
            self.size_bytes = m.get('sizeBytes')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('turnSeq') is not None:
            self.turn_seq = m.get('turnSeq')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

class ListWorkItemArtifactsResponseBodyItemsRef(DaraModel):
    def __init__(
        self,
        id: str = None,
        kind: str = None,
        url: str = None,
    ):
        # The artifact ID.
        self.id = id
        # The reference data type.
        self.kind = kind
        # The OpenAPI artifact access endpoint.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.kind is not None:
            result['kind'] = self.kind

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

