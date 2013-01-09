module KibanaConfig

  # Change which fields are shown by default. Must be set as an array
  # Default_fields = ['@fields.vhost','@fields.response','@fields.request']
  # Just an example. This really makes kibana look much better for your 
  # own usage
  Default_fields = ['@type', '@fields.message']

  # These are set to _all by default.
  # My ES template disables the _all field, so we need to change it here.

  # Primary field. By default Elastic Search has a special
  # field called _all that is searched when no field is specified.
  # Dropping _all can reduce index size significantly. If you do that
  # you'll need to change primary_field to be '@message'
  Primary_field = '@message'

  # Default Elastic Search index to query
  Default_index = '@message'

end
