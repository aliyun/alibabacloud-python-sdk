# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        dry_run: bool = None,
        dry_run_result: bool = None,
        message: str = None,
        order_id: str = None,
        port: str = None,
        request_id: str = None,
        tag_result: bool = None,
        task_id: str = None,
    ):
        # The internal endpoint of the instance.
        self.connection_string = connection_string
        # The instance ID. If the value of the **Amount** parameter is greater than **1**, more than one instance ID is returned. The number of instance IDs that are returned is the same as the value of the Amount parameter. The returned instance IDs are separated by commas (,).
        # 
        # For example, if the value of the **Amount** parameter is **3**, three instance IDs are returned. Examples: `rm-uf6wjk5*****1,rm-uf6wjk5*****2,rm-uf6wjk5*****3`
        self.dbinstance_id = dbinstance_id
        # Indicates that the system performed a dry run.
        # 
        # *   The value is fixed as **true**.
        # *   If the system does not perform a dry run, this parameter is not returned.
        self.dry_run = dry_run
        # Indicates whether the request passed the dry run. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > *   If the system does not perform a dry run, this parameter is not returned.
        # > *   If the request failed the dry run, an error message is returned.
        self.dry_run_result = dry_run_result
        # The message that indicates whether multiple instances are created.
        # 
        # > The parameter is returned only when the value of the **Amount** parameter is greater than 1.
        self.message = message
        # The order ID.
        self.order_id = order_id
        # The internal IP address and port number that are used to connect to the instance.
        self.port = port
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the specified tag is added to the instance. Valid values:
        # 
        # *   **true**: The specified tag is added to the instance.
        # *   **false**: The specified tag fails to be added to the instance.
        # 
        # > If you do not add a tag to the instance, this parameter is not returned.
        self.tag_result = tag_result
        # The ID of the task that is run to create multiple instances.
        # 
        # *   This parameter is returned only when the value of **Amount** is greater than 1.
        # *   The **TaskID** parameter cannot be used to query a task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result

        if self.message is not None:
            result['Message'] = self.message

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tag_result is not None:
            result['TagResult'] = self.tag_result

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DryRunResult') is not None:
            self.dry_run_result = m.get('DryRunResult')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TagResult') is not None:
            self.tag_result = m.get('TagResult')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

