from dataset import DatasetItem

SYHTHETIC_DATASET = [
    DatasetItem(
        text="email contains @gmail.com",
        clarification="We should query documents where the 'email' field contains '@gmail.com'.",
        includes=[
            {"full_name": "jane doe", "email": "jane.doe@gmail.com"},
            {"full_name": "john smith", "email": "john.smith@gmail.com"},
        ],
        excludes=[
            {"full_name": "adam doe", "email": "adam.doe@yahoo.com"},
            {"full_name": "sarah connor", "email": "s.connor@outlook.com"},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "email": {"type": "text"}}
        },
        query={"match": {"email": "@gmail.com"}},
    ),
    DatasetItem(
        text="born after 1990",
        clarification="We should query the 'birth_year' field for values greater than 1990.",
        includes=[
            {"full_name": "jane doe", "birth_year": 1995},
            {"full_name": "john smith", "birth_year": 1992},
        ],
        excludes=[
            {"full_name": "adam doe", "birth_year": 1985},
            {"full_name": "sarah connor", "birth_year": 1980},
        ],
        mappings={
            "properties": {
                "full_name": {"type": "text"},
                "birth_year": {"type": "integer"},
            }
        },
        query={"range": {"birth_year": {"gt": 1990}}},
    ),
    DatasetItem(
        text="find all engineers or doctors",
        clarification="We should query the 'occupation' field for either 'engineer' or 'doctor'.",
        includes=[
            {"full_name": "jane doe", "occupation": "engineer"},
            {"full_name": "john smith", "occupation": "doctor"},
        ],
        excludes=[
            {"full_name": "adam doe", "occupation": "lawyer"},
            {"full_name": "sarah connor", "occupation": "teacher"},
        ],
        mappings={
            "properties": {
                "full_name": {"type": "text"},
                "occupation": {"type": "text"},
            }
        },
        query={
            "bool": {
                "should": [
                    {"match": {"occupation": "engineer"}},
                    {"match": {"occupation": "doctor"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="salary between 50000 and 100000",
        clarification="We should query the 'salary' field for values between 50000 and 100000.",
        includes=[
            {"full_name": "jane doe", "salary": 75000},
            {"full_name": "john smith", "salary": 90000},
        ],
        excludes=[
            {"full_name": "adam doe", "salary": 45000},
            {"full_name": "sarah connor", "salary": 110000},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "salary": {"type": "integer"}}
        },
        query={"range": {"salary": {"gte": 50000, "lte": 100000}}},
    ),
    DatasetItem(
        text="born before 1990",
        clarification="We should query the 'birth_year' field for values less than 1990.",
        includes=[
            {"full_name": "john doe", "birth_year": 1985},
            {"full_name": "jane doe", "birth_year": 1980},
        ],
        excludes=[
            {"full_name": "adam smith", "birth_year": 1995},
            {"full_name": "eva brown", "birth_year": 2000},
        ],
        mappings={
            "properties": {
                "full_name": {"type": "text"},
                "birth_year": {"type": "integer"},
            }
        },
        query={"range": {"birth_year": {"lt": 1990}}},
    ),
    DatasetItem(
        text="name is john or jane",
        clarification="We should perform a full text search on the 'full_name' field for either 'john' or 'jane'.",
        includes=[
            {"full_name": "john doe", "age": 25},
            {"full_name": "jane doe", "age": 30},
        ],
        excludes=[
            {"full_name": "adam smith", "age": 35},
            {"full_name": "eva brown", "age": 40},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "age": {"type": "integer"}}
        },
        query={
            "bool": {
                "should": [
                    {"match": {"full_name": "john"}},
                    {"match": {"full_name": "jane"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="not from New York",
        clarification="We should exclude documents where 'city' field matches 'New York'.",
        includes=[
            {"full_name": "john doe", "city": "Los Angeles"},
            {"full_name": "jane doe", "city": "Chicago"},
        ],
        excludes=[
            {"full_name": "adam smith", "city": "New York"},
            {"full_name": "eva brown", "city": "New York"},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "city": {"type": "text"}}
        },
        query={"bool": {"must_not": {"match": {"city": "New York"}}}},
    ),
    DatasetItem(
        text="age between 25 and 35",
        clarification="We should query the 'age' field for values between 25 and 35.",
        includes=[
            {"full_name": "john doe", "age": 25},
            {"full_name": "jane doe", "age": 35},
        ],
        excludes=[
            {"full_name": "adam smith", "age": 24},
            {"full_name": "eva brown", "age": 36},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "age": {"type": "integer"}}
        },
        query={"range": {"age": {"gte": 25, "lte": 35}}},
    ),
    DatasetItem(
        text="works at Google or Microsoft",
        clarification="We should perform a full text search on the 'company' field for either 'Google' or 'Microsoft'.",
        includes=[
            {"full_name": "john doe", "company": "Google"},
            {"full_name": "jane doe", "company": "Microsoft"},
        ],
        excludes=[
            {"full_name": "adam smith", "company": "Amazon"},
            {"full_name": "eva brown", "company": "Facebook"},
        ],
        mappings={
            "properties": {"full_name": {"type": "text"}, "company": {"type": "text"}}
        },
        query={
            "bool": {
                "should": [
                    {"match": {"company": "Google"}},
                    {"match": {"company": "Microsoft"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="email contains 'example.com'",
        clarification="We should query documents where the 'email' field contains 'example.com'.",
        includes=[
            {"full_name": "Jane Doe", "email": "jane@example.com"},
            {"full_name": "John Smith", "email": "john.smith@example.com"},
        ],
        excludes=[{"full_name": "Adam Johnson", "email": "adam@sample.com"}],
        mappings={"properties": {"email": {"type": "text"}}},
        query={"wildcard": {"email": "*example.com"}},
    ),
    DatasetItem(
        text="status is active or pending",
        clarification="We should query documents where the 'status' field is either 'active' or 'pending'.",
        includes=[
            {"name": "Task 1", "status": "active"},
            {"name": "Task 2", "status": "pending"},
        ],
        excludes=[{"name": "Task 3", "status": "completed"}],
        mappings={"properties": {"status": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"match": {"status": "active"}},
                    {"match": {"status": "pending"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="price between 100 and 200",
        clarification="We should query documents where the 'price' field is between 100 and 200.",
        includes=[
            {"product_name": "Laptop", "price": 150},
            {"product_name": "Tablet", "price": 199},
        ],
        excludes=[
            {"product_name": "Smartphone", "price": 99},
            {"product_name": "Monitor", "price": 201},
        ],
        mappings={"properties": {"price": {"type": "integer"}}},
        query={"range": {"price": {"gte": 100, "lte": 200}}},
    ),
    DatasetItem(
        text="published after 2020",
        clarification="We should query documents where the 'publish_date' field is after the year 2020.",
        includes=[
            {"title": "Future Trends", "publish_date": "2021-05-10"},
            {"title": "Tech Innovations", "publish_date": "2022-01-15"},
        ],
        excludes=[{"title": "Historical Analysis", "publish_date": "2019-08-25"}],
        mappings={"properties": {"publish_date": {"type": "date"}}},
        query={"range": {"publish_date": {"gt": "2020-12-31"}}},
    ),
    DatasetItem(
        text="tagged as urgent and not completed",
        clarification="We should query documents tagged as 'urgent' but not 'completed'.",
        includes=[
            {"task": "Fix critical bug", "tags": ["urgent", "in-progress"]},
            {"task": "Update security protocols", "tags": ["urgent", "pending"]},
        ],
        excludes=[
            {"task": "Routine maintenance", "tags": ["completed"]},
            {"task": "Feature development", "tags": ["in-progress"]},
        ],
        mappings={"properties": {"tags": {"type": "keyword"}}},
        query={
            "bool": {
                "must": {"match": {"tags": "urgent"}},
                "must_not": {"match": {"tags": "completed"}},
            }
        },
    ),
    DatasetItem(
        text="has attachments and priority high",
        clarification="We should query documents that have attachments and are marked as high priority.",
        includes=[
            {
                "email_subject": "Report Submission",
                "has_attachments": True,
                "priority": "high",
            },
            {
                "email_subject": "Project Proposal",
                "has_attachments": True,
                "priority": "high",
            },
        ],
        excludes=[
            {
                "email_subject": "General Inquiry",
                "has_attachments": False,
                "priority": "low",
            },
            {
                "email_subject": "Staff Meeting",
                "has_attachments": True,
                "priority": "low",
            },
        ],
        mappings={
            "properties": {
                "has_attachments": {"type": "boolean"},
                "priority": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"has_attachments": True}},
                    {"match": {"priority": "high"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="books published in 2020",
        clarification="Query should look for 'publication_year' field for exact match.",
        includes=[
            {"title": "Modern Python", "publication_year": 2020},
            {"title": "AI Revolution", "publication_year": 2020},
        ],
        excludes=[
            {"title": "Learning Java", "publication_year": 2019},
            {"title": "History of Computers", "publication_year": 2021},
        ],
        mappings={
            "properties": {
                "title": {"type": "text"},
                "publication_year": {"type": "integer"},
            }
        },
        query={"term": {"publication_year": 2020}},
    ),
    DatasetItem(
        text="price less than 100",
        clarification="Query should find documents where 'price' field is less than 100.",
        includes=[
            {"product_name": "T-shirt", "price": 50},
            {"product_name": "Book", "price": 20},
        ],
        excludes=[
            {"product_name": "Laptop", "price": 1000},
            {"product_name": "Smartphone", "price": 500},
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "price": {"type": "integer"},
            }
        },
        query={"range": {"price": {"lt": 100}}},
    ),
    DatasetItem(
        text="employees in marketing or sales",
        clarification="We should query the 'department' field for either 'marketing' or 'sales'.",
        includes=[
            {"name": "John Doe", "department": "marketing"},
            {"name": "Jane Doe", "department": "sales"},
        ],
        excludes=[
            {"name": "Alice Smith", "department": "engineering"},
            {"name": "Bob Johnson", "department": "finance"},
        ],
        mappings={
            "properties": {"name": {"type": "text"}, "department": {"type": "keyword"}}
        },
        query={
            "bool": {
                "should": [
                    {"match": {"department": "marketing"}},
                    {"match": {"department": "sales"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="not in finance department",
        clarification="We need to exclude documents where 'department' field is 'finance'.",
        includes=[
            {"name": "John Doe", "department": "marketing"},
            {"name": "Jane Doe", "department": "sales"},
        ],
        excludes=[
            {"name": "Alice Smith", "department": "finance"},
            {"name": "Bob Johnson", "department": "finance"},
        ],
        mappings={
            "properties": {"name": {"type": "text"}, "department": {"type": "keyword"}}
        },
        query={"bool": {"must_not": {"match": {"department": "finance"}}}},
    ),
    DatasetItem(
        text="software engineer with 5 years experience",
        clarification="We should match 'position' as 'software engineer' and 'experience' as 5 years.",
        includes=[
            {"name": "John Doe", "position": "software engineer", "experience": 5}
        ],
        excludes=[
            {"name": "Jane Doe", "position": "software engineer", "experience": 3},
            {"name": "Alice Smith", "position": "project manager", "experience": 5},
        ],
        mappings={
            "properties": {
                "name": {"type": "text"},
                "position": {"type": "text"},
                "experience": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"position": "software engineer"}},
                    {"term": {"experience": 5}},
                ]
            }
        },
    ),
    DatasetItem(
        text="red or blue cars",
        clarification="Query should find documents where 'color' field is either 'red' or 'blue'.",
        includes=[
            {"model": "Sedan", "color": "red"},
            {"model": "Coupe", "color": "blue"},
        ],
        excludes=[
            {"model": "Truck", "color": "green"},
            {"model": "SUV", "color": "yellow"},
        ],
        mappings={
            "properties": {"model": {"type": "text"}, "color": {"type": "keyword"}}
        },
        query={
            "bool": {
                "should": [{"match": {"color": "red"}}, {"match": {"color": "blue"}}]
            }
        },
    ),
    DatasetItem(
        text="email ending with @example.com",
        clarification="We should perform a wildcard search on the 'email' field for values ending with '@example.com'.",
        includes=[
            {"email": "user1@example.com", "age": 25},
            {"email": "user2@example.com", "age": 30},
        ],
        excludes=[
            {"email": "user3@sample.com", "age": 35},
            {"email": "user4@notexample.com", "age": 40},
        ],
        mappings={"properties": {"email": {"type": "keyword"}}},
        query={"wildcard": {"email": "*@example.com"}},
    ),
    DatasetItem(
        text="created before 2020",
        clarification="We should query the 'creation_date' field for dates before 2020.",
        includes=[
            {"name": "Document1", "creation_date": "2018-05-20"},
            {"name": "Document2", "creation_date": "2019-11-15"},
        ],
        excludes=[
            {"name": "Document3", "creation_date": "2020-01-25"},
            {"name": "Document4", "creation_date": "2021-07-30"},
        ],
        mappings={"properties": {"creation_date": {"type": "date"}}},
        query={"range": {"creation_date": {"lt": "2020-01-01"}}},
    ),
    DatasetItem(
        text="active users",
        clarification="We should query the 'status' field for the keyword 'active'.",
        includes=[
            {"username": "activeUser1", "status": "active"},
            {"username": "activeUser2", "status": "active"},
        ],
        excludes=[
            {"username": "inactiveUser1", "status": "inactive"},
            {"username": "inactiveUser2", "status": "pending"},
        ],
        mappings={"properties": {"status": {"type": "keyword"}}},
        query={"term": {"status": "active"}},
    ),
    DatasetItem(
        text="books but not ebooks",
        clarification="We should query documents that contain 'books' but exclude those that mention 'ebooks'.",
        includes=[
            {"title": "Physical Books on Science", "format": "paperback"},
            {"title": "Cooking Books", "format": "hardcover"},
        ],
        excludes=[
            {"title": "Ebooks on Programming", "format": "digital"},
            {"title": "Ebooks Collection", "format": "digital"},
        ],
        mappings={
            "properties": {"title": {"type": "text"}, "format": {"type": "keyword"}}
        },
        query={
            "bool": {
                "must": {"match": {"title": "books"}},
                "must_not": {"match": {"title": "ebooks"}},
            }
        },
    ),
    DatasetItem(
        text="science fiction or fantasy",
        clarification="We should query the 'genre' field for documents that are either 'science fiction' or 'fantasy'.",
        includes=[
            {"title": "Space Odyssey", "genre": "science fiction"},
            {"title": "Middle Earth", "genre": "fantasy"},
        ],
        excludes=[
            {"title": "Historical Facts", "genre": "history"},
            {"title": "Cooking 101", "genre": "cooking"},
        ],
        mappings={"properties": {"genre": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"term": {"genre": "science fiction"}},
                    {"term": {"genre": "fantasy"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="published after 2015 and under 500 pages",
        clarification="We should query documents that were published after 2015 and have less than 500 pages.",
        includes=[
            {"title": "Modern Cooking", "published_year": 2018, "pages": 300},
            {"title": "Tech Innovations", "published_year": 2019, "pages": 450},
        ],
        excludes=[
            {"title": "Ancient History", "published_year": 2014, "pages": 600},
            {"title": "Long Novels", "published_year": 2016, "pages": 800},
        ],
        mappings={
            "properties": {
                "published_year": {"type": "integer"},
                "pages": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"published_year": {"gt": 2015}}},
                    {"range": {"pages": {"lt": 500}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="email is john.doe@example.com",
        clarification="We should perform an exact match query on the 'email' field.",
        includes=[{"email": "john.doe@example.com", "age": 28}],
        excludes=[{"email": "jane.doe@example.com", "age": 32}],
        mappings={"properties": {"email": {"type": "keyword"}}},
        query={"term": {"email": "john.doe@example.com"}},
    ),
    DatasetItem(
        text="created after January 1st, 2020",
        clarification="We should query the 'created_at' field with a range greater than a specific date.",
        includes=[{"name": "Document1", "created_at": "2020-05-20"}],
        excludes=[{"name": "Document2", "created_at": "2019-12-31"}],
        mappings={"properties": {"created_at": {"type": "date"}}},
        query={"range": {"created_at": {"gt": "2020-01-01"}}},
    ),
    DatasetItem(
        text="full-time employees",
        clarification="We should query the 'employment_type' field for the value 'full-time'.",
        includes=[{"name": "John Doe", "employment_type": "full-time"}],
        excludes=[{"name": "Jane Doe", "employment_type": "part-time"}],
        mappings={"properties": {"employment_type": {"type": "keyword"}}},
        query={"term": {"employment_type": "full-time"}},
    ),
    DatasetItem(
        text="has email and phone number",
        clarification="We should use 'must' to ensure both fields are present.",
        includes=[
            {"name": "John Doe", "email": "john@example.com", "phone": "1234567890"}
        ],
        excludes=[
            {"name": "Jane Doe", "email": "jane@example.com"},
            {"name": "Jake Doe"},
        ],
        mappings={
            "properties": {"email": {"type": "keyword"}, "phone": {"type": "keyword"}}
        },
        query={
            "bool": {
                "must": [{"exists": {"field": "email"}}, {"exists": {"field": "phone"}}]
            }
        },
    ),
    DatasetItem(
        text="engineering department but not manager",
        clarification="We should use 'must' for department and 'must_not' for role.",
        includes=[
            {"name": "John Doe", "department": "engineering", "role": "engineer"}
        ],
        excludes=[
            {"name": "Jane Doe", "department": "engineering", "role": "manager"},
            {"name": "Jake Doe", "department": "sales", "role": "salesperson"},
        ],
        mappings={
            "properties": {
                "department": {"type": "keyword"},
                "role": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [{"term": {"department": "engineering"}}],
                "must_not": [{"term": {"role": "manager"}}],
            }
        },
    ),
    DatasetItem(
        text="software or hardware department",
        clarification="We should use 'should' to match documents belonging to either department.",
        includes=[
            {"name": "John Doe", "department": "software"},
            {"name": "Jane Doe", "department": "hardware"},
        ],
        excludes=[{"name": "Jake Doe", "department": "sales"}],
        mappings={"properties": {"department": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"term": {"department": "software"}},
                    {"term": {"department": "hardware"}},
                ],
                "minimum_should_match": 1,
            }
        },
    ),
    DatasetItem(
        text="registered before 2020",
        clarification="We should query the 'registration_date' field for dates before 2020.",
        includes=[
            {"full_name": "John Doe", "registration_date": "2015-06-01"},
            {"full_name": "Jane Smith", "registration_date": "2018-09-15"},
        ],
        excludes=[
            {"full_name": "Adam White", "registration_date": "2020-01-20"},
            {"full_name": "Emily Johnson", "registration_date": "2021-07-22"},
        ],
        mappings={"properties": {"registration_date": {"type": "date"}}},
        query={"range": {"registration_date": {"lt": "2020-01-01"}}},
    ),
    DatasetItem(
        text="active and premium users",
        clarification="We should use a boolean query to find users who are active and have a premium account.",
        includes=[
            {"username": "active_premium_1", "active": True, "premium": True},
            {"username": "active_premium_2", "active": True, "premium": True},
        ],
        excludes=[
            {"username": "inactive_user", "active": False, "premium": True},
            {"username": "regular_active", "active": True, "premium": False},
        ],
        mappings={
            "properties": {
                "active": {"type": "boolean"},
                "premium": {"type": "boolean"},
            }
        },
        query={
            "bool": {
                "must": [{"match": {"active": True}}, {"match": {"premium": True}}]
            }
        },
    ),
    DatasetItem(
        text="find users named John or Jane",
        clarification="We should use an OR condition to find users whose name is either John or Jane.",
        includes=[
            {"full_name": "John Doe", "age": 30},
            {"full_name": "Jane Smith", "age": 25},
        ],
        excludes=[
            {"full_name": "Adam Johnson", "age": 35},
            {"full_name": "Emily White", "age": 28},
        ],
        mappings={"properties": {"full_name": {"type": "text"}}},
        query={
            "bool": {
                "should": [
                    {"match": {"full_name": "John"}},
                    {"match": {"full_name": "Jane"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="employees but not managers",
        clarification="We should exclude managers from the search result.",
        includes=[
            {"position": "developer", "name": "John Doe"},
            {"position": "designer", "name": "Jane Smith"},
        ],
        excludes=[
            {"position": "manager", "name": "Adam Johnson"},
            {"position": "senior manager", "name": "Emily White"},
        ],
        mappings={"properties": {"position": {"type": "text"}}},
        query={"bool": {"must_not": {"match": {"position": "manager"}}}},
    ),
    DatasetItem(
        text="salary between 50000 and 80000",
        clarification="We should query the 'salary' field for values between 50000 and 80000.",
        includes=[
            {"name": "John Doe", "salary": 60000},
            {"name": "Jane Smith", "salary": 75000},
        ],
        excludes=[
            {"name": "Adam Johnson", "salary": 45000},
            {"name": "Emily White", "salary": 85000},
        ],
        mappings={"properties": {"salary": {"type": "integer"}}},
        query={"range": {"salary": {"gte": 50000, "lte": 80000}}},
    ),
    DatasetItem(
        text="find documents with tag 'urgent' or 'high-priority'",
        clarification="We're looking for documents tagged as either 'urgent' or 'high-priority'.",
        includes=[
            {"title": "Urgent report", "tags": ["urgent", "finance"]},
            {"title": "Important meeting", "tags": ["high-priority", "meeting"]},
        ],
        excludes=[
            {"title": "Weekly summary", "tags": ["summary", "finance"]},
            {"title": "General assembly", "tags": ["meeting"]},
        ],
        mappings={"properties": {"tags": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"term": {"tags": "urgent"}},
                    {"term": {"tags": "high-priority"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="software engineer in New York",
        clarification="We should match both job title as 'software engineer' and location as 'New York'.",
        includes=[
            {
                "job_title": "software engineer",
                "location": "New York",
                "salary": 120000,
            },
            {
                "job_title": "senior software engineer",
                "location": "New York",
                "salary": 150000,
            },
        ],
        excludes=[
            {
                "job_title": "software engineer",
                "location": "San Francisco",
                "salary": 130000,
            },
            {"job_title": "data scientist", "location": "New York", "salary": 110000},
        ],
        mappings={
            "properties": {
                "job_title": {"type": "text"},
                "location": {"type": "keyword"},
                "salary": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"job_title": "software engineer"}},
                    {"term": {"location": "New York"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="published after 2015",
        clarification="We should query the 'publication_date' field for dates after 2015.",
        includes=[
            {"title": "Modern AI Techniques", "publication_date": "2018-06-12"},
            {"title": "Deep Learning Advances", "publication_date": "2020-01-25"},
        ],
        excludes=[
            {"title": "Introduction to Algorithms", "publication_date": "2009-05-15"},
            {"title": "Data Structures in C", "publication_date": "1999-07-21"},
        ],
        mappings={
            "properties": {
                "title": {"type": "text"},
                "publication_date": {"type": "date"},
            }
        },
        query={"range": {"publication_date": {"gt": "2015-01-01"}}},
    ),
    DatasetItem(
        text="email not verified",
        clarification="We should look for users whose 'email_verified' status is false.",
        includes=[
            {"username": "user123", "email_verified": False},
            {"username": "john_doe", "email_verified": False},
        ],
        excludes=[
            {"username": "verified_user", "email_verified": True},
            {"username": "jane_doe", "email_verified": True},
        ],
        mappings={
            "properties": {
                "username": {"type": "keyword"},
                "email_verified": {"type": "boolean"},
            }
        },
        query={"term": {"email_verified": False}},
    ),
    DatasetItem(
        text="price between 100 and 500",
        clarification="Query the 'price' field for values between 100 and 500.",
        includes=[
            {"product_name": "Wireless Headphones", "price": 150},
            {"product_name": "Bluetooth Speaker", "price": 300},
        ],
        excludes=[
            {"product_name": "Laptop", "price": 800},
            {"product_name": "USB Cable", "price": 20},
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "price": {"type": "integer"},
            }
        },
        query={"range": {"price": {"gte": 100, "lte": 500}}},
    ),
    DatasetItem(
        text="find documents with 'urgent' or 'immediate' in title",
        clarification="We should match documents where the title contains either 'urgent' or 'immediate'.",
        includes=[
            {"title": "Urgent: Update Required", "status": "pending"},
            {"title": "Immediate Action Needed", "status": "open"},
        ],
        excludes=[
            {"title": "Regular Update", "status": "closed"},
            {"title": "Scheduled Maintenance", "status": "open"},
        ],
        mappings={
            "properties": {"title": {"type": "text"}, "status": {"type": "keyword"}}
        },
        query={
            "bool": {
                "should": [
                    {"match": {"title": "urgent"}},
                    {"match": {"title": "immediate"}},
                ],
                "minimum_should_match": 1,
            }
        },
    ),
    DatasetItem(
        text="products under $50",
        clarification="We should query products with a price less than 50.",
        includes=[
            {"product_name": "T-shirt", "price": 25},
            {"product_name": "Book", "price": 20},
        ],
        excludes=[{"product_name": "Jacket", "price": 60}],
        mappings={"properties": {"price": {"type": "integer"}}},
        query={"range": {"price": {"lt": 50}}},
    ),
    DatasetItem(
        text="email from john.doe@example.com",
        clarification="We need an exact match query for the 'email' field.",
        includes=[{"email": "john.doe@example.com", "subject": "Meeting Schedule"}],
        excludes=[{"email": "jane.doe@example.com", "subject": "Project Plan"}],
        mappings={"properties": {"email": {"type": "keyword"}}},
        query={"term": {"email": "john.doe@example.com"}},
    ),
    DatasetItem(
        text="employees in finance department",
        clarification="We should query the 'department' field for the text 'finance'.",
        includes=[{"name": "John Smith", "department": "finance"}],
        excludes=[{"name": "Jane Doe", "department": "marketing"}],
        mappings={"properties": {"department": {"type": "text"}}},
        query={"match": {"department": "finance"}},
    ),
    DatasetItem(
        text="documents created after January 1, 2020",
        clarification="We should query the 'created_date' field for dates after January 1, 2020.",
        includes=[{"title": "Annual Report", "created_date": "2020-05-01"}],
        excludes=[{"title": "Old Inventory List", "created_date": "2019-11-15"}],
        mappings={"properties": {"created_date": {"type": "date"}}},
        query={"range": {"created_date": {"gt": "2020-01-01"}}},
    ),
    DatasetItem(
        text="active user accounts",
        clarification="We should query the 'status' field for the boolean value true.",
        includes=[{"username": "johnsmith", "status": True}],
        excludes=[{"username": "inactiveuser", "status": False}],
        mappings={"properties": {"status": {"type": "boolean"}}},
        query={"term": {"status": True}},
    ),
    DatasetItem(
        text="find reports containing budget and forecast",
        clarification="We need a query that matches documents containing both 'budget' and 'forecast'.",
        includes=[
            {
                "title": "2021 Budget Forecast",
                "content": "This report contains both budget and forecast figures.",
            }
        ],
        excludes=[
            {
                "title": "2021 Budget",
                "content": "This report contains only budget figures.",
            }
        ],
        mappings={"properties": {"content": {"type": "text"}}},
        query={
            "bool": {
                "must": [
                    {"match": {"content": "budget"}},
                    {"match": {"content": "forecast"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="projects without status completed",
        clarification="We should exclude documents where the 'status' field matches 'completed'.",
        includes=[{"project_name": "New Website", "status": "in progress"}],
        excludes=[{"project_name": "Marketing Campaign", "status": "completed"}],
        mappings={"properties": {"status": {"type": "keyword"}}},
        query={"bool": {"must_not": {"term": {"status": "completed"}}}},
    ),
    DatasetItem(
        text="vacation requests in July or August",
        clarification="We should find documents where the 'month' field matches either 'July' or 'August'.",
        includes=[
            {"employee": "John Doe", "month": "July"},
            {"employee": "Jane Smith", "month": "August"},
        ],
        excludes=[{"employee": "Mike Brown", "month": "September"}],
        mappings={"properties": {"month": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [{"term": {"month": "July"}}, {"term": {"month": "August"}}]
            }
        },
    ),
    DatasetItem(
        text="products priced between 50 and 100",
        clarification="We should query the 'price' field for products within the 50 to 100 range.",
        includes=[
            {"name": "Product A", "price": 75},
            {"name": "Product B", "price": 50},
        ],
        excludes=[
            {"name": "Product C", "price": 49},
            {"name": "Product D", "price": 101},
        ],
        mappings={"properties": {"price": {"type": "integer"}}},
        query={"range": {"price": {"gte": 50, "lte": 100}}},
    ),
    DatasetItem(
        text="available blue products",
        clarification="We need to find products that are both available and blue. This requires an AND condition.",
        includes=[{"name": "Blue Shirt", "color": "blue", "available": True}],
        excludes=[
            {"name": "Red Shirt", "color": "red", "available": True},
            {"name": "Blue Pants", "color": "blue", "available": False},
        ],
        mappings={
            "properties": {
                "color": {"type": "keyword"},
                "available": {"type": "boolean"},
            }
        },
        query={
            "bool": {
                "must": [{"match": {"color": "blue"}}, {"match": {"available": True}}]
            }
        },
    ),
    DatasetItem(
        text="manager or director titles",
        clarification="We should find documents where the title is either manager or director.",
        includes=[
            {"name": "John Doe", "title": "Sales Manager"},
            {"name": "Jane Doe", "title": "Marketing Director"},
        ],
        excludes=[{"name": "Sam Smith", "title": "Engineer"}],
        mappings={"properties": {"title": {"type": "text"}}},
        query={
            "bool": {
                "should": [
                    {"match": {"title": "manager"}},
                    {"match": {"title": "director"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="employees not in sales department",
        clarification="We should exclude employees in the sales department.",
        includes=[
            {"name": "John Doe", "department": "Engineering"},
            {"name": "Jane Doe", "department": "Marketing"},
        ],
        excludes=[{"name": "Sam Smith", "department": "Sales"}],
        mappings={"properties": {"department": {"type": "keyword"}}},
        query={"bool": {"must_not": {"match": {"department": "Sales"}}}},
    ),
    DatasetItem(
        text="articles published after 2020",
        clarification="Query articles with a publish date after 2020.",
        includes=[
            {"title": "Future of AI", "publish_date": "2021-05-20"},
            {"title": "Advancements in Robotics", "publish_date": "2022-01-15"},
        ],
        excludes=[{"title": "Technology in 2010s", "publish_date": "2019-12-31"}],
        mappings={"properties": {"publish_date": {"type": "date"}}},
        query={"range": {"publish_date": {"gt": "2020-12-31"}}},
    ),
    DatasetItem(
        text="active users with more than 1000 followers",
        clarification="We need to find users who are active and have more than 1000 followers.",
        includes=[{"username": "user1", "followers": 1500, "active": True}],
        excludes=[
            {"username": "user2", "followers": 500, "active": True},
            {"username": "user3", "followers": 2000, "active": False},
        ],
        mappings={
            "properties": {
                "followers": {"type": "integer"},
                "active": {"type": "boolean"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"followers": {"gt": 1000}}},
                    {"match": {"active": True}},
                ]
            }
        },
    ),
    DatasetItem(
        text="books published after 2010",
        clarification="We should query the 'publish_date' field for dates after 2010.",
        includes=[
            {"title": "Modern AI Techniques", "publish_date": "2015-06-17"},
            {"title": "Advanced Robotics", "publish_date": "2013-09-25"},
        ],
        excludes=[{"title": "Introduction to Computing", "publish_date": "2005-04-12"}],
        mappings={"properties": {"publish_date": {"type": "date"}}},
        query={"range": {"publish_date": {"gt": "2010-01-01"}}},
    ),
    DatasetItem(
        text="products with more than 100 units in stock",
        clarification="We should query the 'stock' field for values greater than 100.",
        includes=[
            {"product_name": "Laptop", "stock": 150},
            {"product_name": "Smartphone", "stock": 200},
        ],
        excludes=[{"product_name": "Tablet", "stock": 50}],
        mappings={"properties": {"stock": {"type": "integer"}}},
        query={"range": {"stock": {"gt": 100}}},
    ),
    DatasetItem(
        text="find documents where the project is either 'Apollo' or 'Gemini'",
        clarification="We should use the 'OR' operator to query the 'project_name' field for either 'Apollo' or 'Gemini'.",
        includes=[
            {"document_title": "Apollo Mission Summary", "project_name": "Apollo"},
            {"document_title": "Gemini Spacecraft Overview", "project_name": "Gemini"},
        ],
        excludes=[
            {"document_title": "Skylab Technical Analysis", "project_name": "Skylab"}
        ],
        mappings={"properties": {"project_name": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"term": {"project_name": "Apollo"}},
                    {"term": {"project_name": "Gemini"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="sales reports for Q2 and Q3",
        clarification="We should use the 'OR' operator to query the 'quarter' field for either 'Q2' or 'Q3'.",
        includes=[
            {"report_name": "Q2 Sales Report", "quarter": "Q2"},
            {"report_name": "Q3 Sales Report", "quarter": "Q3"},
        ],
        excludes=[{"report_name": "Q1 Sales Report", "quarter": "Q1"}],
        mappings={"properties": {"quarter": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [{"term": {"quarter": "Q2"}}, {"term": {"quarter": "Q3"}}]
            }
        },
    ),
    DatasetItem(
        text="email from example.com",
        clarification="We should query the 'email' field for addresses belonging to example.com domain.",
        includes=[
            {"name": "John Doe", "email": "john.doe@example.com"},
            {"name": "Jane Doe", "email": "jane.doe@example.com"},
        ],
        excludes=[
            {"name": "Adam Smith", "email": "adam.smith@otherdomain.com"},
            {"name": "Eve Black", "email": "eve.black@anotherdomain.com"},
        ],
        mappings={
            "properties": {"name": {"type": "text"}, "email": {"type": "keyword"}}
        },
        query={"wildcard": {"email": "*@example.com"}},
    ),
    DatasetItem(
        text="employees hired after 2015",
        clarification="We should query the 'hire_date' field for employees hired after the year 2015.",
        includes=[
            {"name": "John Doe", "hire_date": "2016-05-10"},
            {"name": "Jane Smith", "hire_date": "2019-07-01"},
        ],
        excludes=[
            {"name": "Adam Johnson", "hire_date": "2010-03-15"},
            {"name": "Eve Davidson", "hire_date": "2005-09-23"},
        ],
        mappings={
            "properties": {"name": {"type": "text"}, "hire_date": {"type": "date"}}
        },
        query={"range": {"hire_date": {"gt": "2015-12-31"}}},
    ),
    DatasetItem(
        text="return items with warranty",
        clarification="We should query the 'warranty' field for items that have a warranty.",
        includes=[
            {"product_name": "Laptop", "warranty": True},
            {"product_name": "Smartphone", "warranty": True},
        ],
        excludes=[
            {"product_name": "Book", "warranty": False},
            {"product_name": "Pen", "warranty": False},
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "warranty": {"type": "boolean"},
            }
        },
        query={"match": {"warranty": True}},
    ),
    DatasetItem(
        text="find documents tagged urgent or critical",
        clarification="We should query the 'tags' field for documents tagged as 'urgent' or 'critical'.",
        includes=[
            {"title": "Server Down Report", "tags": ["urgent", "server"]},
            {"title": "Security Breach", "tags": ["critical", "security"]},
        ],
        excludes=[
            {"title": "Weekly Newsletter", "tags": ["information", "news"]},
            {"title": "Holiday Schedule", "tags": ["announcement", "news"]},
        ],
        mappings={
            "properties": {"title": {"type": "text"}, "tags": {"type": "keyword"}}
        },
        query={
            "bool": {
                "should": [
                    {"match": {"tags": "urgent"}},
                    {"match": {"tags": "critical"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="products in category electronics",
        clarification="Query should target 'category' field with exact match, using 'keyword' type for precision.",
        includes=[
            {"product_name": "Smartphone", "category": "electronics", "price": 999}
        ],
        excludes=[
            {"product_name": "Blender", "category": "home appliances", "price": 59}
        ],
        mappings={"properties": {"category": {"type": "keyword"}}},
        query={"term": {"category": "electronics"}},
    ),
    DatasetItem(
        text="emails received after 2022-01-01",
        clarification="Query should target 'received_date' field for dates after 2022-01-01.",
        includes=[
            {
                "subject": "Meeting Schedule",
                "sender": "boss@example.com",
                "received_date": "2022-01-02",
            }
        ],
        excludes=[
            {
                "subject": "Year End Party",
                "sender": "hr@example.com",
                "received_date": "2021-12-30",
            }
        ],
        mappings={"properties": {"received_date": {"type": "date"}}},
        query={"range": {"received_date": {"gt": "2022-01-01"}}},
    ),
    DatasetItem(
        text="active users with more than 1000 points",
        clarification="Query should target 'status' field for active users and 'points' field for users with more than 1000 points.",
        includes=[{"username": "john_doe", "status": "active", "points": 1500}],
        excludes=[
            {"username": "jane_doe", "status": "inactive", "points": 2000},
            {"username": "bob_smith", "status": "active", "points": 900},
        ],
        mappings={
            "properties": {"status": {"type": "keyword"}, "points": {"type": "integer"}}
        },
        query={
            "bool": {
                "must": [
                    {"term": {"status": "active"}},
                    {"range": {"points": {"gt": 1000}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="available products under 50 dollars",
        clarification="Query should target 'price' field for products under 50 dollars and 'availability' field for available products.",
        includes=[{"product_name": "Notebook", "price": 45, "availability": True}],
        excludes=[
            {"product_name": "Pen", "price": 3, "availability": False},
            {"product_name": "Desk Lamp", "price": 55, "availability": True},
        ],
        mappings={
            "properties": {
                "price": {"type": "integer"},
                "availability": {"type": "boolean"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"price": {"lt": 50}}},
                    {"term": {"availability": True}},
                ]
            }
        },
    ),
    DatasetItem(
        text="find employees hired before 2015",
        clarification="Query should target 'hire_date' field for employees hired before the year 2015.",
        includes=[{"employee_name": "Alice Johnson", "hire_date": "2014-11-01"}],
        excludes=[{"employee_name": "Bob Smith", "hire_date": "2015-02-20"}],
        mappings={"properties": {"hire_date": {"type": "date"}}},
        query={"range": {"hire_date": {"lt": "2015-01-01"}}},
    ),
    DatasetItem(
        text="search for blue or green t-shirts",
        clarification="Query should target 'color' field for t-shirts that are either blue or green.",
        includes=[
            {"product_name": "Summer T-Shirt", "color": "blue"},
            {"product_name": "Spring T-Shirt", "color": "green"},
        ],
        excludes=[{"product_name": "Autumn T-Shirt", "color": "red"}],
        mappings={"properties": {"color": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [{"term": {"color": "blue"}}, {"term": {"color": "green"}}],
                "minimum_should_match": 1,
            }
        },
    ),
    DatasetItem(
        text="urgent and high priority tickets",
        clarification="Query should target 'priority' and 'status' fields for tickets that are both urgent and of high priority.",
        includes=[{"ticket_id": "TCK12345", "priority": "high", "status": "urgent"}],
        excludes=[
            {"ticket_id": "TCK54321", "priority": "low", "status": "urgent"},
            {"ticket_id": "TCK67890", "priority": "high", "status": "normal"},
        ],
        mappings={
            "properties": {
                "priority": {"type": "keyword"},
                "status": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [{"term": {"priority": "high"}}, {"term": {"status": "urgent"}}]
            }
        },
    ),
    DatasetItem(
        text="emails from john.doe@example.com",
        clarification="Need to query 'sender_email' field for a specific email address.",
        includes=[
            {"subject": "Meeting Schedule", "sender_email": "john.doe@example.com"},
            {"subject": "Project Plan", "sender_email": "john.doe@example.com"},
        ],
        excludes=[{"subject": "Annual Report", "sender_email": "jane.doe@example.com"}],
        mappings={
            "properties": {
                "subject": {"type": "text"},
                "sender_email": {"type": "keyword"},
            }
        },
        query={"term": {"sender_email": "john.doe@example.com"}},
    ),
    DatasetItem(
        text="products in category 'electronics' not made by 'Acme Corp'",
        clarification="Need to filter by 'category' and exclude items by 'manufacturer'.",
        includes=[
            {
                "product_name": "Smartphone",
                "category": "electronics",
                "manufacturer": "Gadgets Inc",
            },
            {
                "product_name": "Laptop",
                "category": "electronics",
                "manufacturer": "Tech Innovations",
            },
        ],
        excludes=[
            {
                "product_name": "Tablet",
                "category": "electronics",
                "manufacturer": "Acme Corp",
            },
            {
                "product_name": "Smartphone",
                "category": "home appliances",
                "manufacturer": "Gadgets Inc",
            },
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "category": {"type": "keyword"},
                "manufacturer": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [{"term": {"category": "electronics"}}],
                "must_not": [{"term": {"manufacturer": "Acme Corp"}}],
            }
        },
    ),
    DatasetItem(
        text="vacation rentals available between July 1 and July 15",
        clarification="Query should find rentals where the available dates overlap with the given range, using a 'range' query on a 'date' field.",
        includes=[
            {
                "title": "Beachfront Condo",
                "available_start": "2023-07-01",
                "available_end": "2023-07-10",
            },
            {
                "title": "Mountain Cabin",
                "available_start": "2023-07-05",
                "available_end": "2023-07-20",
            },
        ],
        excludes=[
            {
                "title": "City Apartment",
                "available_start": "2023-06-20",
                "available_end": "2023-06-30",
            },
            {
                "title": "Country House",
                "available_start": "2023-07-16",
                "available_end": "2023-07-25",
            },
        ],
        mappings={
            "properties": {
                "title": {"type": "text"},
                "available_start": {"type": "date"},
                "available_end": {"type": "date"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"available_start": {"lte": "2023-07-15"}}},
                    {"range": {"available_end": {"gte": "2023-07-01"}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="Find all products in category 'Electronics' with a price over 1000",
        clarification="We should query both 'category' and 'price' fields, using a bool query to combine conditions.",
        includes=[
            {"product_name": "Laptop Pro", "category": "Electronics", "price": 1500},
            {"product_name": "Smart TV", "category": "Electronics", "price": 1200},
        ],
        excludes=[
            {"product_name": "Coffee Maker", "category": "Kitchen", "price": 150},
            {"product_name": "E-Reader", "category": "Electronics", "price": 200},
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "category": {"type": "keyword"},
                "price": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"category": "Electronics"}},
                    {"range": {"price": {"gt": 1000}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="Search for employees hired after 2015 who work in the 'Sales' department",
        clarification="We should use a bool query to combine a range query on 'hire_date' and a match query on 'department'.",
        includes=[
            {"full_name": "Jane Doe", "department": "Sales", "hire_date": "2016-05-22"},
            {
                "full_name": "John Smith",
                "department": "Sales",
                "hire_date": "2017-03-15",
            },
        ],
        excludes=[
            {
                "full_name": "Alice Johnson",
                "department": "Marketing",
                "hire_date": "2018-07-04",
            },
            {
                "full_name": "Bob Brown",
                "department": "Sales",
                "hire_name": "2014-02-20",
            },
        ],
        mappings={
            "properties": {
                "full_name": {"type": "text"},
                "department": {"type": "keyword"},
                "hire_date": {"type": "date"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"hire_date": {"gt": "2015-01-01"}}},
                    {"match": {"department": "Sales"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="Retrieve all transactions above 5000 that were either in 'USD' or 'EUR'",
        clarification="This requires a bool query with a must clause for the range and a should clause for the currency, ensuring at least one match on currency.",
        includes=[
            {"transaction_id": "T1001", "amount": 5500, "currency": "USD"},
            {"transaction_id": "T1002", "amount": 6000, "currency": "EUR"},
        ],
        excludes=[
            {"transaction_id": "T1003", "amount": 4500, "currency": "USD"},
            {"transaction_id": "T1004", "amount": 7000, "currency": "JPY"},
        ],
        mappings={
            "properties": {
                "transaction_id": {"type": "keyword"},
                "amount": {"type": "integer"},
                "currency": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [{"range": {"amount": {"gt": 5000}}}],
                "should": [
                    {"match": {"currency": "USD"}},
                    {"match": {"currency": "EUR"}},
                ],
                "minimum_should_match": 1,
            }
        },
    ),
    DatasetItem(
        text="Find documents created in 2021 that are tagged as 'urgent' or 'high priority'",
        clarification="We need to combine a range query for the creation year with a bool query for the tags.",
        includes=[
            {
                "document_id": "D001",
                "tags": ["urgent", "confidential"],
                "creation_year": 2021,
            },
            {"document_id": "D002", "tags": ["high priority"], "creation_year": 2021},
        ],
        excludes=[
            {"document_id": "D003", "tags": ["normal"], "creation_year": 2021},
            {"document_id": "D004", "tags": ["urgent"], "creation_year": 2019},
        ],
        mappings={
            "properties": {
                "document_id": {"type": "keyword"},
                "tags": {"type": "keyword"},
                "creation_year": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [{"range": {"creation_year": {"gte": 2021, "lte": 2021}}}],
                "should": [
                    {"match": {"tags": "urgent"}},
                    {"match": {"tags": "high priority"}},
                ],
                "minimum_should_match": 1,
            }
        },
    ),
    DatasetItem(
        text="products priced between 50 and 100 in electronics category",
        clarification="We should query the 'price' field for a range and 'category' field for a match.",
        includes=[
            {
                "product_name": "Wireless Headphones",
                "price": 75,
                "category": "electronics",
            },
            {
                "product_name": "Bluetooth Speaker",
                "price": 60,
                "category": "electronics",
            },
        ],
        excludes=[
            {"product_name": "Wireless Mouse", "price": 25, "category": "electronics"},
            {"product_name": "Smartphone", "price": 150, "category": "electronics"},
        ],
        mappings={
            "properties": {
                "price": {"type": "integer"},
                "category": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"price": {"gte": 50, "lte": 100}}},
                    {"match": {"category": "electronics"}},
                ]
            }
        },
    ),
    DatasetItem(
        text="recent transactions above 1000 USD after January 1, 2021",
        clarification="Query the 'amount' field for values above 1000 and 'date' for dates after January 1, 2021.",
        includes=[
            {
                "transaction_id": "tx123",
                "amount": 1500,
                "currency": "USD",
                "date": "2021-05-20",
            },
            {
                "transaction_id": "tx124",
                "amount": 2000,
                "currency": "USD",
                "date": "2021-03-15",
            },
        ],
        excludes=[
            {
                "transaction_id": "tx125",
                "amount": 900,
                "currency": "USD",
                "date": "2021-07-22",
            },
            {
                "transaction_id": "tx126",
                "amount": 1100,
                "currency": "USD",
                "date": "2020-12-30",
            },
        ],
        mappings={
            "properties": {
                "amount": {"type": "integer"},
                "currency": {"type": "keyword"},
                "date": {"type": "date"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"range": {"amount": {"gt": 1000}}},
                    {"range": {"date": {"gt": "2021-01-01"}}},
                ],
                "filter": [{"term": {"currency": "USD"}}],
            }
        },
    ),
    DatasetItem(
        text="find documents with status active but exclude those tagged urgent or confidential",
        clarification="Must match documents where the 'status' is active and must not include documents tagged as urgent or confidential.",
        includes=[
            {
                "document_id": "doc123",
                "status": "active",
                "tags": ["review", "external"],
            },
            {"document_id": "doc124", "status": "active", "tags": ["internal"]},
        ],
        excludes=[
            {"document_id": "doc125", "status": "active", "tags": ["urgent"]},
            {"document_id": "doc126", "status": "active", "tags": ["confidential"]},
        ],
        mappings={
            "properties": {"status": {"type": "keyword"}, "tags": {"type": "keyword"}}
        },
        query={
            "bool": {
                "must": [{"match": {"status": "active"}}],
                "must_not": [{"terms": {"tags": ["urgent", "confidential"]}}],
            }
        },
    ),
    DatasetItem(
        text="employees in the IT department located in New York or San Francisco",
        clarification="We should match employees in the IT department and filter those located in New York or San Francisco.",
        includes=[
            {"employee_id": "emp123", "department": "IT", "location": "New York"},
            {"employee_id": "emp124", "department": "IT", "location": "San Francisco"},
        ],
        excludes=[
            {"employee_id": "emp125", "department": "IT", "location": "Chicago"},
            {
                "employee_id": "emp126",
                "department": "Marketing",
                "location": "New York",
            },
        ],
        mappings={
            "properties": {
                "department": {"type": "keyword"},
                "location": {"type": "keyword"},
            }
        },
        query={
            "bool": {
                "must": [{"match": {"department": "IT"}}],
                "filter": [{"terms": {"location": ["New York", "San Francisco"]}}],
            }
        },
    ),
    DatasetItem(
        text="articles published in 2020 or 2021 by author John Doe or Jane Doe",
        clarification="Query must match articles by the authors John Doe or Jane Doe and filter those published in 2020 or 2021.",
        includes=[
            {"article_id": "art123", "author": "John Doe", "publish_year": 2020},
            {"article_id": "art124", "author": "Jane Doe", "publish_year": 2021},
        ],
        excludes=[
            {"article_id": "art125", "author": "John Doe", "publish_year": 2019},
            {"article_id": "art126", "author": "Alice Smith", "publish_year": 2020},
        ],
        mappings={
            "properties": {
                "author": {"type": "keyword"},
                "publish_year": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [{"terms": {"author": ["John Doe", "Jane Doe"]}}],
                "filter": [{"terms": {"publish_year": [2020, 2021]}}],
            }
        },
    ),
    DatasetItem(
        text="email from domain example.com",
        clarification="We should filter emails by domain, looking for 'example.com'.",
        includes=[{"email": "user1@example.com"}, {"email": "user2@example.com"}],
        excludes=[
            {"email": "user@anotherdomain.com"},
            {"email": "example@notexample.com"},
        ],
        mappings={"properties": {"email": {"type": "keyword"}}},
        query={"wildcard": {"email": "*@example.com"}},
    ),
    DatasetItem(
        text="active users with more than 100 followers",
        clarification="Query should find active users ('status': 'active') with followers count over 100.",
        includes=[
            {"username": "activeUser1", "status": "active", "followers": 150},
            {"username": "activeUser2", "status": "active", "followers": 200},
        ],
        excludes=[
            {"username": "inactiveUser", "status": "inactive", "followers": 120},
            {"username": "activeUserLowFollowers", "status": "active", "followers": 50},
        ],
        mappings={
            "properties": {
                "status": {"type": "keyword"},
                "followers": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"status": "active"}},
                    {"range": {"followers": {"gt": 100}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="products in category Electronics with price between 100 and 500",
        clarification="Query should filter products within 'Electronics' category and price range 100-500.",
        includes=[
            {"product_name": "Smartphone", "category": "Electronics", "price": 299},
            {"product_name": "Tablet", "category": "Electronics", "price": 450},
        ],
        excludes=[
            {"product_name": "Smartphone", "category": "Electronics", "price": 99},
            {"product_name": "Tablet", "category": "Home Appliances", "price": 200},
        ],
        mappings={
            "properties": {
                "category": {"type": "keyword"},
                "price": {"type": "integer"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"category": "Electronics"}},
                    {"range": {"price": {"gte": 100, "lte": 500}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="events in New York next week",
        clarification="Query for events with 'location' in New York and 'date' next week.",
        includes=[
            {"event_name": "Tech Meetup", "location": "New York", "date": "2023-05-15"},
            {
                "event_name": "Art Exhibition",
                "location": "New York",
                "date": "2023-05-17",
            },
        ],
        excludes=[
            {
                "event_name": "Tech Meetup",
                "location": "San Francisco",
                "date": "2023-05-15",
            },
            {
                "event_name": "Art Exhibition",
                "location": "New York",
                "date": "2023-06-20",
            },
        ],
        mappings={
            "properties": {"location": {"type": "keyword"}, "date": {"type": "date"}}
        },
        query={
            "bool": {
                "must": [
                    {"match": {"location": "New York"}},
                    {"range": {"date": {"gte": "2023-05-14", "lte": "2023-05-21"}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="return items with missing descriptions",
        clarification="We need to find items where the 'description' field is missing.",
        includes=[
            {"product_name": "Unnamed Product", "category": "Miscellaneous"},
            {"product_name": "No Description", "category": "General"},
        ],
        excludes=[
            {
                "product_name": "Complete Product",
                "category": "Electronics",
                "description": "Fully described product.",
            },
            {
                "product_name": "Described Item",
                "category": "Home Appliances",
                "description": "This item has a description.",
            },
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "category": {"type": "keyword"},
                "description": {"type": "text"},
            }
        },
        query={"bool": {"must_not": {"exists": {"field": "description"}}}},
    ),
    DatasetItem(
        text="products in stock under $50",
        clarification="Query 'in_stock' field for true and 'price' field for values under 50.",
        includes=[
            {"product_name": "Wireless Mouse", "in_stock": True, "price": 29.99},
            {"product_name": "USB Keyboard", "in_stock": True, "price": 45.5},
        ],
        excludes=[
            {"product_name": "Gaming Monitor", "in_stock": True, "price": 250.0},
            {"product_name": "Wireless Mouse", "in_stock": False, "price": 29.99},
        ],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "in_stock": {"type": "boolean"},
                "price": {"type": "float"},
            }
        },
        query={
            "bool": {
                "must": [
                    {"match": {"in_stock": True}},
                    {"range": {"price": {"lt": 50}}},
                ]
            }
        },
    ),
    DatasetItem(
        text="events in 2021",
        clarification="Query 'event_date' for dates within the year 2021.",
        includes=[
            {"event_name": "Tech Conference", "event_date": "2021-05-20"},
            {"event_name": "Science Fair", "event_date": "2021-08-15"},
        ],
        excludes=[
            {"event_name": "New Year Party", "event_date": "2020-12-31"},
            {"event_name": "Halloween Bash", "event_date": "2022-10-31"},
        ],
        mappings={
            "properties": {
                "event_name": {"type": "text"},
                "event_date": {"type": "date"},
            }
        },
        query={"range": {"event_date": {"gte": "2021-01-01", "lte": "2021-12-31"}}},
    ),
    DatasetItem(
        text="products with stock below 50",
        clarification="We need to find products where the 'stock' field is less than 50.",
        includes=[
            {"product_name": "Laptop Sleeve", "stock": 20},
            {"product_name": "Wireless Mouse", "stock": 45},
        ],
        excludes=[{"product_name": "USB-C Adapter", "stock": 150}],
        mappings={
            "properties": {
                "product_name": {"type": "text"},
                "stock": {"type": "integer"},
            }
        },
        query={"range": {"stock": {"lt": 50}}},
    ),
    DatasetItem(
        text="transactions in 2022",
        clarification="Query should target transactions with a 'date' in the year 2022.",
        includes=[
            {"transaction_id": "TX1001", "amount": 150.0, "date": "2022-05-20"},
            {"transaction_id": "TX1002", "amount": 200.0, "date": "2022-11-15"},
        ],
        excludes=[{"transaction_id": "TX1003", "amount": 100.0, "date": "2023-01-10"}],
        mappings={
            "properties": {
                "transaction_id": {"type": "keyword"},
                "amount": {"type": "float"},
                "date": {"type": "date"},
            }
        },
        query={"range": {"date": {"gte": "2022-01-01", "lte": "2022-12-31"}}},
    ),
    DatasetItem(
        text="emails containing 'urgent'",
        clarification="We should search within the 'email_body' field for the term 'urgent'.",
        includes=[
            {
                "email_body": "This is an urgent request, please respond ASAP.",
                "sender": "jane.doe@example.com",
            }
        ],
        excludes=[
            {
                "email_body": "Looking forward to our meeting next week.",
                "sender": "john.smith@example.com",
            }
        ],
        mappings={"properties": {"email_body": {"type": "text"}}},
        query={"match": {"email_body": "urgent"}},
    ),
    DatasetItem(
        text="products priced over 100",
        clarification="Query should target the 'price' field for values greater than 100.",
        includes=[
            {"product_name": "Laptop", "price": 1200},
            {"product_name": "Smartphone", "price": 800},
        ],
        excludes=[{"product_name": "Mousepad", "price": 20}],
        mappings={"properties": {"price": {"type": "integer"}}},
        query={"range": {"price": {"gt": 100}}},
    ),
    DatasetItem(
        text="stock lower than 50",
        clarification="We should focus on querying the 'stock' field for values less than 50.",
        includes=[{"product_name": "Tea Cups", "stock": 30}],
        excludes=[{"product_name": "Coffee Mugs", "stock": 150}],
        mappings={"properties": {"stock": {"type": "integer"}}},
        query={"range": {"stock": {"lt": 50}}},
    ),
    DatasetItem(
        text="high priority tickets",
        clarification="We're querying for tickets with a priority marked as 'high'.",
        includes=[{"ticket_id": "TCK10023", "priority": "high"}],
        excludes=[{"ticket_id": "TCK10024", "priority": "low"}],
        mappings={"properties": {"priority": {"type": "keyword"}}},
        query={"match": {"priority": "high"}},
    ),
    DatasetItem(
        text="completed tasks",
        clarification="We're looking for tasks that have been marked as completed.",
        includes=[{"task_name": "Update website", "status": "completed"}],
        excludes=[{"task_name": "Fix login issue", "status": "in progress"}],
        mappings={"properties": {"status": {"type": "keyword"}}},
        query={"match": {"status": "completed"}},
    ),
    DatasetItem(
        text="employees hired before 2015",
        clarification="Query for employees with 'hire_date' before 2015.",
        includes=[{"name": "Jane Doe", "hire_date": "2012-06-01"}],
        excludes=[{"name": "John Smith", "hire_date": "2016-09-15"}],
        mappings={"properties": {"hire_date": {"type": "date"}}},
        query={"range": {"hire_date": {"lt": "2015-01-01"}}},
    ),
    DatasetItem(
        text="articles tagged as 'AI' or 'Machine Learning'",
        clarification="Query for articles where 'tags' field contains either 'AI' or 'Machine Learning'.",
        includes=[{"title": "Deep Learning Advances", "tags": ["AI", "Deep Learning"]}],
        excludes=[{"title": "General Science", "tags": ["Science"]}],
        mappings={"properties": {"tags": {"type": "keyword"}}},
        query={
            "bool": {
                "should": [
                    {"term": {"tags": "AI"}},
                    {"term": {"tags": "Machine Learning"}},
                ]
            }
        },
    ),
]
