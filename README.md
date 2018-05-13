<p>
	Welcome on this small ugly website. 
	<br> To better navigate the site, here are some indications :
		<br>The nav bar can be used to access different options
		<br> <ul>
			<li>Welcome brings you to this homepage</li>
			<li>read csv charge to content of the csv file into the database</li>
			<li>run apply a 15 years run on the model and store the results in the database</li>
			<li>filter results helps you visualize the database and you can use filters on it too</li>
			<li>delete cleans the database, deleting all stored data (you can still refill it using read csv afterwards)</li>
		</ul>
		<br><p>
			To answer the test, the idea was to create a platform where people could load their csv and run their models. I used the Django framework for this, as it has a lot of built-in interesting options (like abstracting objects and Query from databases). If you are unfamiliar with Django use: <a href="https://www.tutorialspoint.com/django/django_overview.htm">this website</a> to set it up. Note that I let it in a non-production state to better debug and to better understand the code.
			<br>How to improve this website:
			<ul>
				<li>use CSS/Jquery/Bootstraps as it is really ugly right now</li>
				<li>create a form that allow users to load their own csv directly on the site</li>
				<li>add more filters for a better data-visualization (like to observe each agent's evolution independently)</li>
				<li>Use a real database : django is right now using sqlite, and while it is convenient, it is however slower than postgres for instance</li>
				<li>regarding the database, reduce some field's sizes (the results column only needs 15 bits right now)</li>
				<li>note : The first time I tried to load all the datas in sqlite, my pc (which is quite old) nearly froze for 15+ minutes... <br>So make sure to optimize as much as possible the data access (I reduced this latence by using a bulk insertion instead of a row-per-row, it now only takes a few seconds on my pc to load it)</li>
			</ul>
			<br>Expendability:
			<ul>
				<li>It is quite easy to change the number of years for which the model runs. Eventually, we could pass it as a parameter instead of using 15 all the time<br> The results of the run are stored in an integer field using bitwise operations, so the adaptation would be really easy (no need to modify the database) </li>
				<li>It woulb be easy to load another set of data with this platform. Eventually we could even run different types of models on different types of agents</li>
			</ul>
		</p>
		<p>
			For a better use of the website, note that:
			<ul>
				<li>It is useless to filter the results without loading the csv first (as the DB is empty)</li>
				<li>It is also useless to filter per year before running the model, as the results are 0 per default (so it will print all the DB as if it was Breed_NC)(actually it would be great to have either a boolean to indicate wether it was already runned or not, or to run it automatically after insertion of the data, but to make it easier to read i'll let it like that for now)</li>
				<li>You have to check the checkboxes if you want to select each or each type of agent</li>
				<li>note that you can filter by age, you have to enter the age of an agent a t=0. Therefore if you want to see those who'll be 60 at year = 3, enter age=57 and year=3</li>
			</ul>
		</p>
</p>