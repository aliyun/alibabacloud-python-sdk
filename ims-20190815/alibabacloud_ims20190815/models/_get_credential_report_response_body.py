# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCredentialReportResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        generated_time: str = None,
        is_truncated: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The content of the user credential report.
        # 
        # The report is Base64-encoded. After you decode the report, the credential report is in the CSV format.
        self.content = content
        # The time when the user credential report was generated.
        self.generated_time = generated_time
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The parameter that is used to obtain the truncated part. This parameter takes effect only when `IsTruncated` is set to true.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.generated_time is not None:
            result['GeneratedTime'] = self.generated_time

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GeneratedTime') is not None:
            self.generated_time = m.get('GeneratedTime')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

