# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataResultsValue(DaraModel):
    def __init__(
        self,
        route_id: str = None,
        status: str = None,
        error_message: str = None,
    ):
        # The route ID corresponding to the result, which is the same as the key in results.
        self.route_id = route_id
        # For asynchronous publishing, Pending indicates that the request is accepted, and Rejected indicates that the request is rejected before submission. For synchronous publishing, Succeeded indicates that the route is successfully published, and Failed indicates that the publishing failed.
        self.status = status
        # The cause of the route being rejected or failing to be published. This parameter is returned when the status is Rejected or Failed.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_id is not None:
            result['routeId'] = self.route_id

        if self.status is not None:
            result['status'] = self.status

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        return self

