# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Point(Model):
    """Point.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. Timestamp of a data point. Please make sure it
     aligns with the midnight, and use a UTC date time string, e.g.,
     2017-08-01T00:00:00Z.
    :type timestamp: datetime
    :param value: Required. The measurement of that point, should be float.
    :type value: float
    """

    _validation = {
        'timestamp': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'Timestamp', 'type': 'iso-8601'},
        'value': {'key': 'Value', 'type': 'float'},
    }

    def __init__(self, *, timestamp, value: float, **kwargs) -> None:
        super(Point, self).__init__(**kwargs)
        self.timestamp = timestamp
        self.value = value
