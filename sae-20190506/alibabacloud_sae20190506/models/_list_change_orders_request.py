# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChangeOrdersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        co_status: str = None,
        co_type: str = None,
        current_page: int = None,
        key: str = None,
        order_by: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        # 1
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the request.
        self.co_status = co_status
        # The type of the change order. Valid values:
        # 
        # *   **CoBindSlb**: associates the Server Load Balancer (SLB) instance with the application.
        # *   **CoUnbindSlb**: disassociates an SLB instance from the application.
        # *   **CoCreateApp**: creates the application.
        # *   **CoDeleteApp**: deletes the application.
        # *   **CoDeploy**: deploys the application.
        # *   **CoRestartApplication**: restarts the application.
        # *   **CoRollback**: rolls back the application.
        # *   **CoScaleIn**: scales in the application.
        # *   **CoScaleOut**: scales out the application.
        # *   **CoStartApplication**: starts the application.
        # *   **CoStopApplication**: stops the application.
        # *   **CoRescaleApplicationVertically**: modifies the instance type.
        # *   **CoDeployHistroy**: rolls back the application to an earlier version.
        # *   **CoBindNas**: associates a network-attached storage (NAS) file system with the application.
        # *   **CoUnbindNas**: disassociates a NAS file system from the application.
        # *   **CoBatchStartApplication**: starts multiple applications concurrently.
        # *   **CoBatchStopApplication**: stops multiple applications concurrently.
        # *   **CoRestartInstances**: restarts the instance.
        # *   **CoDeleteInstances**: deletes the instance.
        # *   **CoScaleInAppWithInstances**: reduces the specified number of application instances.
        self.co_type = co_type
        # 20
        self.current_page = current_page
        # CoCreateApp
        self.key = key
        self.order_by = order_by
        # test
        self.page_size = page_size
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.co_status is not None:
            result['CoStatus'] = self.co_status

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.key is not None:
            result['Key'] = self.key

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        return self

