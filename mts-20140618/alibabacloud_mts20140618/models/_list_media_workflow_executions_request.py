# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaWorkflowExecutionsRequest(DaraModel):
    def __init__(
        self,
        input_file_url: str = None,
        maximum_page_size: int = None,
        media_workflow_id: str = None,
        media_workflow_name: str = None,
        next_page_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The Object Storage Service (OSS) URL of the input file of the media workflow. The URL complies with RFC 3986 and is encoded in UTF-8, with reserved characters being percent-encoded. For more information, see [URL encoding](https://help.aliyun.com/document_detail/423796.html).
        self.input_file_url = input_file_url
        # The maximum number of media workflow execution instances to return. Valid values: `[1,100]`. Default value: **10**.
        self.maximum_page_size = maximum_page_size
        # The ID of the media workflow whose execution instances you want to query. To obtain the workflow ID, you can log on to the **ApsaraVideo Media Processing (MPS) console** and choose **Workflows** > **Workflow Settings**.
        self.media_workflow_id = media_workflow_id
        # The name of the media workflow. To obtain the workflow name, you can log on to the **MPS console** and choose **Workflows** > **Workflow Settings**.
        self.media_workflow_name = media_workflow_name
        # The pagination token that is used in the next request to retrieve a new page of results. The value is a UUID that contains 32 characters. When you request the first page of query results, leave the NextPageToken parameter empty. When you request more query results, specify the value of the NextPageToken parameter returned in the query results on the previous page.
        self.next_page_token = next_page_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file_url is not None:
            result['InputFileURL'] = self.input_file_url

        if self.maximum_page_size is not None:
            result['MaximumPageSize'] = self.maximum_page_size

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.media_workflow_name is not None:
            result['MediaWorkflowName'] = self.media_workflow_name

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFileURL') is not None:
            self.input_file_url = m.get('InputFileURL')

        if m.get('MaximumPageSize') is not None:
            self.maximum_page_size = m.get('MaximumPageSize')

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('MediaWorkflowName') is not None:
            self.media_workflow_name = m.get('MediaWorkflowName')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

