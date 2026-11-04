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
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The status of the change order. Valid values:
        # 
        # - **0**: preparing
        # - **1**: executing
        # - **2**: executed successfully
        # - **3**: execution failed
        # - **6**: terminated
        # - **8**: waiting for manual batch confirmation
        # - **9**: waiting for automatic batch confirmation
        # - **10**: execution failed due to a system exception
        # - **11**: waiting for approval
        # - **12**: approved and waiting for execution
        self.co_status = co_status
        # The type of the change order. Valid values:
        # 
        # - **CoBindSlb**: bind an SLB instance
        # - **CoUnbindSlb**: unbind an SLB instance
        # - **CoCreateApp**: create an application
        # - **CoDeleteApp**: delete an application
        # - **CoDeploy**: deploy an application
        # - **CoRestartApplication**: restart an application
        # - **CoRollback**: roll back an application
        # - **CoScaleIn**: scale in an application
        # - **CoScaleOut**: scale out an application
        # - **CoStartApplication**: start an application
        # - **CoStopApplication**: stop an application
        # - **CoRescaleApplicationVertically**: change instance specifications
        # - **CoDeployHistroy**: roll back to a historical version
        # - **CoBindNas**: bind a NAS file system
        # - **CoUnbindNas**: unbind a NAS file system
        # - **CoBatchStartApplication**: start applications in batches
        # - **CoBatchStopApplication**: stop applications in batches
        # - **CoRestartInstances**: restart instances
        # - **CoDeleteInstances**: delete instances
        # - **CoScaleInAppWithInstances**: scale in specified instances
        self.co_type = co_type
        # The current page number.
        self.current_page = current_page
        # The keyword used for fuzzy match of the change order description. Change orders whose descriptions contain the keyword are returned.
        self.key = key
        # The sorting condition.
        self.order_by = order_by
        # The number of entries per page.
        self.page_size = page_size
        # Specifies whether to sort the results in ascending order based on the field specified by the **OrderBy** parameter. Valid values:
        # 
        #   - **true**: sort in ascending order
        #   - **false**: sort in descending order
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

