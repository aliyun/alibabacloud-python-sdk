# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BatchRequest(DaraModel):
    def __init__(
        self,
        requests: List[main_models.BatchRequestRequests] = None,
        resource: str = None,
    ):
        # The child requests.
        # 
        # The number of child requests. Valid value: 1 to 100.
        # 
        # This parameter is required.
        self.requests = requests
        # The type of the resource that you want to manage. Valid values:
        # 
        # *   file: a file.
        # *   drive: an individual drive or a team drive.
        # *   user: a user.
        # *   group: a group.
        # *   membership: a group member.
        # *   share_link: a share.
        # *   async_task: an asynchronous task.
        # 
        # This parameter is required.
        self.resource = resource

    def validate(self):
        if self.requests:
            for v1 in self.requests:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['requests'] = []
        if self.requests is not None:
            for k1 in self.requests:
                result['requests'].append(k1.to_map() if k1 else None)

        if self.resource is not None:
            result['resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.requests = []
        if m.get('requests') is not None:
            for k1 in m.get('requests'):
                temp_model = main_models.BatchRequestRequests()
                self.requests.append(temp_model.from_map(k1))

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        return self

class BatchRequestRequests(DaraModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        id: str = None,
        method: str = None,
        url: str = None,
    ):
        # The request parameters of a child request. The parameter value must be a JSON string. For more information, see the topic of the corresponding child request.
        # 
        # Before you specify the request body, you must specify a header by using Content-Type. Content-Type can only be set to application/json.
        self.body = body
        # The header of a child request, which indicates the type of the data specified in the request body.
        self.headers = headers
        # The ID of the child request. The ID is used to associate a child request with a response. The ID of a child request must be unique.
        # 
        # This parameter is required.
        self.id = id
        # The method of a child request. Valid values:
        # 
        # *   POST
        # *   GET
        # *   PUT
        # *   DELETE
        # *   HEAD
        # 
        # This parameter is required.
        self.method = method
        # The API path of a child request. Valid values:
        # 
        # *   /file/get: queries the information about a file.
        # *   /file/update: modifies the information about a file.
        # *   /file/search: searches for a file.
        # *   /file/copy: copies a file or folder.
        # *   /file/move: moves a file or folder.
        # *   /file/delete: deletes a file or folder.
        # *   /file/get_download_url: queries the download URL of a file.
        # *   /file/get_share_link_download_url: queries the download URL of a file in a share.
        # *   /recyclebin/trash: moves a file or folder to the recycle bin.
        # *   /recyclebin/restore: restores a file or folder.
        # *   /file/put_usertags: adds tags to a user.
        # *   /file/delete_usertags: removes tags from a user.
        # *   /drive/get: queries the information about a drive.
        # *   /user/get: queries the information about a user.
        # *   /group/get: queries the information about a group.
        # *   /share_link/create: creates a share.
        # *   /share_link/update: modifies a share.
        # *   /share_link/cancel: cancels a share.
        # *   /share_link/list: queries shares.
        # *   /share_link/get: queries the information about a share.
        # *   /share_link/get_share_token: queries an access token of a share.
        # *   /async_task/get: queries the information about an asynchronous task.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.headers is not None:
            result['headers'] = self.headers

        if self.id is not None:
            result['id'] = self.id

        if self.method is not None:
            result['method'] = self.method

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

