flask-admin-s3-upload with special function
=====================

Field types for allowing file and image uploads to Amazon S3 (as well as default local storage) in Flask-Admin.


Example
-------

For a complete, working Flask app that demonstrates flask-admin-s3-upload in action, have a look at `flask-s3-save-example <https://github.com/Jaza/flask-s3-save-example>`_.


Usage
-----

Use with a Flask-Admin ModelView by overriding field types, and by passing in special arguments to those fields:

.. code-block:: python

    from flask.ext.admin.contrib.sqla import ModelView

    class MyView(ModelView):
        form_overrides = dict(
            some_image=S3ImageUploadField,
            some_file=S3FileUploadField)

        form_args = dict(
            some_image=dict(
                base_path='/some/folder/static',
                relative_path='some_image/',
                url_relative_path='uploads/',
                namegen=your_namegen_func_here,
                storage_type_field='some_image_storage_type',
                bucket_name_field='some_image_storage_bucket_name',
            ),
            some_file=dict(
                base_path='/some/folder/static',
                relative_path='some_file/',
                namegen=your_namegen_func_here,
                allowed_extensions=('pdf', 'txt'),
                storage_type_field='some_file_storage_type',
                bucket_name_field='some_file_storage_bucket_name',
            ))

        def scaffold_form(self):
            # Note: assuming that we have Flask-S3 config values to pass
            # to fields below. Flask-S3 is not required, you can pass
            # values from elsewhere if you want.
            from flask import current_app as app

            form_class = super(MyView, self).scaffold_form()
            static_root_parent = '/some/folder'

            if app.config['USE_S3']:
                form_class.some_image.kwargs['storage_type'] = 's3'
                form_class.some_file.kwargs['storage_type'] = 's3'

            form_class.some_image.kwargs['bucket_name'] = app.config['S3_BUCKET_NAME']
            form_class.some_image.kwargs['access_key_id'] = app.config['AWS_ACCESS_KEY_ID']
            form_class.some_image.kwargs['access_key_secret'] = app.config['AWS_SECRET_ACCESS_KEY']
            form_class.some_image.kwargs['static_root_parent'] = static_root_parent

            form_class.some_file.kwargs['bucket_name'] = app.config['S3_BUCKET_NAME']
            form_class.some_file.kwargs['access_key_id'] = app.config['AWS_ACCESS_KEY_ID']
            form_class.some_file.kwargs['access_key_secret'] = app.config['AWS_SECRET_ACCESS_KEY']
            form_class.some_file.kwargs['static_root_parent'] = static_root_parent

            return form_class
