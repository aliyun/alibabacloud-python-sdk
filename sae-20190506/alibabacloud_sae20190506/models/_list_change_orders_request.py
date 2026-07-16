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
        # - **0**: Preparing.
        # 
        # - **1**: In progress.
        # 
        # - **2**: Succeeded.
        # 
        # - **3**: Failed.
        # 
        # - **6**: Stopped.
        # 
        # - **8**: Paused for manual confirmation.
        # 
        # - **9**: Paused for automatic confirmation.
        # 
        # - **10**: Failed due to a system exception.
        # 
        # - **11**: Pending approval.
        # 
        # - **12**: Approved and pending execution.
        self.co_status = co_status
        # The type of the change order. Valid values:
        # 
        # - **CoBindSlb**: Attach an SLB instance.
        # 
        # - **CoUnbindSlb**: Detach an SLB instance.
        # 
        # - **CoCreateApp**: Create an application.
        # 
        # - **CoDeleteApp**: Delete an application.
        # 
        # - **CoDeploy**: Deploy an application.
        # 
        # - **CoRestartApplication**: Restart an application.
        # 
        # - **CoRollback**: Roll back an application.
        # 
        # - **CoScaleIn**: Scale in an application.
        # 
        # - **CoScaleOut**: Scale out an application.
        # 
        # - **CoStartApplication**: Start an application.
        # 
        # - **CoStopApplication**: Stop an application.
        # 
        # - **CoRescaleApplicationVertically**: Change the instance type.
        # 
        # - **CoDeployHistroy**: Roll back to a previous version.
        # 
        # - **CoBindNas**: Attach a NAS file system.
        # 
        # - **CoUnbindNas**: Detach a NAS file system.
        # 
        # - **CoBatchStartApplication**: Batch start applications.
        # 
        # - **CoBatchStopApplication**: Batch stop applications.
        # 
        # - **CoRestartInstances**: Restart instances.
        # 
        # - **CoDeleteInstances**: Delete instances.
        # 
        # - **CoScaleInAppWithInstances**: Scale in an application by specifying instances.
        self.co_type = co_type
        # The current page number.
        self.current_page = current_page
        # The keyword for a fuzzy search of change order descriptions. The operation returns only the change orders whose descriptions contain the **keyword**.
        self.key = key
        # The field by which to sort the results.
        self.order_by = order_by
        # The number of entries to return on each page.
        self.page_size = page_size
        # The sort order for the field specified by the **OrderBy** parameter. Valid values:
        # 
        # - **true**: The results are sorted in ascending order.
        # 
        # - **false**: The results are sorted in descending order.
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

