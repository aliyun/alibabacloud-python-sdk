# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpsertChunksResponseBody(DaraModel):
    def __init__(
        self,
        embedding_tokens: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # Number of tokens used during vectorization.
        # 
        # > A token refers to the smallest unit into which the input text is divided. A token can be a word, a phrase, a punctuation mark, a character, etc.
        self.embedding_tokens = embedding_tokens
        self.job_id = job_id
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # API execution status, with the following values:
        # - **success**: Execution succeeded.
        # - **fail**: Execution failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

